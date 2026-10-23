"""NOIR review model. Original JPG is embedded unchanged as a UV atlas.
Requires numpy/scipy. Geometry is an interpretation, not a production pattern.
"""
from pathlib import Path
import json, struct, math
import numpy as np
from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator

ROOT = Path(__file__).resolve().parent
# Coordinates on the provided design sheet, expressed at 1792 x 1396.
# Counterclockwise tracing: neckline, right sleeve, hem, left sleeve.
outline = np.array([
 [878,211],[924,214],[970,208],[1000,223],[1075,262],
 [1224,323],[1196,426],[1106,399],[1106,776],
 [1030,793],[926,804],[825,791],[749,777],[749,400],
 [660,425],[631,323],[779,264],[852,218]
],float)
# Neck, cuff openings, and bottom hem stay open. Other edges meet at a seam.
open_edges={0,1,5,8,9,10,11,14,17}
seams=[(outline[i],outline[(i+1)%len(outline)]) for i in range(len(outline)) if i not in open_edges]

def inside(p):
 x,y=p; result=False
 for a,b in zip(outline,np.roll(outline,-1,axis=0)):
  if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]: result=not result
 return result

def segdist(p,a,b):
 t=np.clip(np.dot(p-a,b-a)/np.dot(b-a,b-a),0,1)
 return np.linalg.norm(p-(a+t*(b-a)))

points=[]; edge_ids=[]
for i,(a,b) in enumerate(zip(outline,np.roll(outline,-1,axis=0))):
 ids=[]
 for t in np.linspace(0,1,max(2,int(np.linalg.norm(b-a)/6)),endpoint=False):
  ids.append(len(points)); points.append(a+(b-a)*t)
 edge_ids.append(ids)
boundary_count=len(points)
for y in np.arange(217,800,7):
 for x in np.arange(636+(3.5 if int(y)%2 else 0),1220,7):
  if inside((x,y)): points.append([x,y])
points=np.array(points)
tri=Delaunay(points).simplices
tri=np.array([t for t in tri if inside(points[t].mean(axis=0)) and all(inside(points[t[[i,(i+1)%3]]].mean(axis=0)) or min(segdist(points[t[[i,(i+1)%3]]].mean(axis=0),a,b) for a,b in zip(outline,np.roll(outline,-1,axis=0)))<.1 for i in range(3))])

# Separate rear pattern landmarks prevent the sheet background leaking onto shoulders.
rear_outline=np.array([[1480,402],[1436,406],[1390,400],[1369,416],[1290,446],
 [1139,515],[1169,646],[1259,617],[1259,971],[1330,988],[1436,998],
 [1537,987],[1615,973],[1615,617],[1706,646],[1732,515],[1584,446],[1508,415]],float)
landmarks=np.vstack([outline,[[927,350],[927,550],[927,750],[770,550],[1080,550]]])
rear_landmarks=np.vstack([rear_outline,[[1436,543],[1436,744],[1436,945],[1594,744],[1282,744]]])
rear_uv=LinearNDInterpolator(landmarks,rear_landmarks)
positions=[]; uvs=[]; indices=[]
for back in [False,True]:
 for px,py in points:
  x=(px-927)/530; y=(804-py)/550-.55
  distance=min(segdist(np.array([px,py]),a,b) for a,b in seams)/530
  depth=.135 if abs(x)<.32 else .095
  z=depth*math.sqrt(min(1,max(0,distance/.105)))
  # Small drape deformation; folds taper out at sewn edges.
  wave=(.004*math.sin(35*y+8*x)+.003*math.sin(61*x-12*y))
  wave+=.006*math.sin(25*x+11*y)*max(0,(-y-.1)/.45)
  z=max(0,z+wave*min(1,distance/.04))
  if back: z=-z*.88
  positions.append([x,y,z])
  # Exact source sheet artwork, no generated logo substitutes.
  if not back: uvs.append([px/1792,py/1396])
  else:
   # Rear artwork's torso has slightly different proportions on the sheet.
   bx,by=rear_uv([px,py])[0]
   uvs.append([bx/1792,by/1396])
 for t in tri:
  a,b,c=t
  ab=points[b]-points[a]; ac=points[c]-points[a]
  if ab[0]*ac[1]-ab[1]*ac[0]>0: b,c=c,b
  indices.extend(([int(a+len(points)),int(c+len(points)),int(b+len(points))] if back else [int(a),int(b),int(c)]))
# Join front/back at perimeter sewn edges; leave sleeves, hem and neck open.
for i,ids in enumerate(edge_ids):
 if i in open_edges: continue
 ids=ids+[edge_ids[(i+1)%len(edge_ids)][0]]
 for a,b in zip(ids,ids[1:]):
  indices.extend([a,b,a+len(points),b,b+len(points),a+len(points)])

# Build a raised fold-over polo collar as a separate white textile surface.
# Dimensions inferred from reference, not a manufacturing specification.
collar_pos=[]; collar_uv=[]; collar_idx=[]
N=96; R=8
for row in range(R+1):
 t=row/R
 for j in range(N+1):
  theta=2*math.pi*j/N
  front=max(0,math.cos(theta))
  rx=.097+.040*t; rz=.079+.044*t
  x=rx*math.sin(theta)
  y=.536-.084*t-.043*front*t
  z=rz*math.cos(theta)
  collar_pos.append([x,y,z]); collar_uv.append([0,0])
for row in range(R):
 for j in range(N):
  a=row*(N+1)+j; b=a+N+1
  collar_idx.extend([a,b,a+1,a+1,b,b+1])

def normals(p,idx):
 p=np.array(p,dtype=np.float32); n=np.zeros_like(p)
 for t in np.array(idx).reshape(-1,3):
  normal=np.cross(p[t[1]]-p[t[0]],p[t[2]]-p[t[0]])
  n[t]+=normal
 norm=np.linalg.norm(n,axis=1); norm[norm==0]=1
 return n/norm[:,None]

# GLB 2.0, self-contained JPG texture, standard PBR materials.
blob=bytearray(); views=[]; accessors=[]
def add_data(data,target=None):
 while len(blob)%4: blob.append(0)
 offset=len(blob); blob.extend(data)
 view={'buffer':0,'byteOffset':offset,'byteLength':len(data)}
 if target: view['target']=target
 views.append(view); return len(views)-1

def accessor(values,kind):
 if kind=='SCALAR': ar=np.array(values,dtype='<u4'); comp=5125; target=34963
 else: ar=np.array(values,dtype='<f4'); comp=5126; target=34962
 view=add_data(ar.tobytes(),target)
 item={'bufferView':view,'componentType':comp,'count':len(ar),'type':kind}
 if kind=='VEC3': item.update(min=ar.min(axis=0).tolist(),max=ar.max(axis=0).tolist())
 accessors.append(item); return len(accessors)-1

# Interior cloth is plain shaded red rather than a mirrored printed sheet.
outer_normals=normals(positions,indices)
inner_positions=(np.array(positions)-outer_normals*.0015).tolist()
inner_indices=np.array(indices).reshape(-1,3)[:,[0,2,1]].reshape(-1).tolist()
primitives=[]
for p,uv,idx,material in [(positions,uvs,indices,0),(collar_pos,collar_uv,collar_idx,1),(inner_positions,uvs,inner_indices,2)]:
 # Remove collapsed triangles where the pattern edges meet.
 pp=np.array(p); tt=np.array(idx).reshape(-1,3)
 area=np.linalg.norm(np.cross(pp[tt[:,1]]-pp[tt[:,0]],pp[tt[:,2]]-pp[tt[:,0]]),axis=1)
 idx=tt[area>1e-10].reshape(-1).tolist()
 primitives.append({'attributes':{'POSITION':accessor(p,'VEC3'),'NORMAL':accessor(normals(p,idx),'VEC3'),'TEXCOORD_0':accessor(uv,'VEC2')},'indices':accessor(idx,'SCALAR'),'material':material})
img_view=add_data((ROOT/'design-reference.jpg').read_bytes())
doc={'asset':{'version':'2.0','generator':'NOIR review model builder','extras':{'status':'Concept geometry; side construction and drape inferred. Original design-sheet artwork embedded unchanged.'}},'scene':0,'scenes':[{'nodes':[0]}],'nodes':[{'mesh':0,'name':'NOIR Budak Gang — review model'}],'meshes':[{'primitives':primitives}], 'materials':[{'name':'Original jersey artwork','doubleSided':False,'pbrMetallicRoughness':{'baseColorTexture':{'index':0},'metallicFactor':0,'roughnessFactor':.92}},{'name':'White collar textile','doubleSided':True,'pbrMetallicRoughness':{'baseColorFactor':[.94,.94,.92,1],'metallicFactor':0,'roughnessFactor':.95}},{'name':'Interior cloth — inferred','doubleSided':False,'pbrMetallicRoughness':{'baseColorFactor':[.30,.023,.029,1],'metallicFactor':0,'roughnessFactor':1}}], 'textures':[{'source':0,'sampler':0}],'samplers':[{'magFilter':9729,'minFilter':9987,'wrapS':33071,'wrapT':33071}],'images':[{'bufferView':img_view,'mimeType':'image/jpeg'}],'accessors':accessors,'bufferViews':views,'buffers':[{'byteLength':len(blob)}]}
js=json.dumps(doc,separators=(',',':')).encode(); js+=b' '*((-len(js))%4); blob.extend(b'\0'*((-len(blob))%4))
output=struct.pack('<III',0x46546c67,2,12+8+len(js)+8+len(blob))+struct.pack('<II',len(js),0x4e4f534a)+js+struct.pack('<II',len(blob),0x004e4942)+blob
(ROOT/'noir-jersey-v1.glb').write_bytes(output)
print(f'Model exported: {len(output)/1024/1024:.2f} MB')
