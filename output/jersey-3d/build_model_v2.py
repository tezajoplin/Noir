"""Editable full-volume garment reconstruction from the supplied design sheet.

Artwork is sampled unchanged. Construction and cloth drape are inferred;
this is a review reconstruction, not a measured production garment.
"""
from pathlib import Path
import json
import math
import struct
import numpy as np

ROOT = Path(__file__).resolve().parent
parts = []


def normals(vertices, faces):
    vertices = np.asarray(vertices, dtype=np.float32)
    faces = np.asarray(faces).reshape(-1, 3)
    result = np.zeros_like(vertices)
    cross = np.cross(vertices[faces[:, 1]] - vertices[faces[:, 0]],
                     vertices[faces[:, 2]] - vertices[faces[:, 0]])
    for column in range(3):
        np.add.at(result, faces[:, column], cross)
    lengths = np.linalg.norm(result, axis=1)
    return result / np.maximum(lengths[:, None], 1e-8)


def surface(rows, columns, point, material=0, inside=True):
    positions, uv, faces = [], [], []
    for row in range(rows + 1):
        for col in range(columns + 1):
            position, texcoord = point(row / rows, col / columns)
            positions.append(position)
            uv.append(texcoord)
    for row in range(rows):
        for col in range(columns):
            a = row * (columns + 1) + col
            b = a + columns + 1
            faces.extend([a, a + 1, b, a + 1, b + 1, b])
    positions = np.asarray(positions)
    faces = np.asarray(faces).reshape(-1, 3)
    n = normals(positions, faces)
    # Orient cloth toward the exterior, using radial distance from the body.
    if np.mean(np.sum(n[:, [0, 2]] * positions[:, [0, 2]], axis=1)) < 0:
        faces = faces[:, [0, 2, 1]]
        n = -n
    parts.append((positions, uv, faces.flatten(), n, material))
    if inside:
        parts.append((positions - n * .0018, uv,
                      faces[:, [0, 2, 1]].flatten(), -n, 2))


def torso_uv(x, y, back):
    if back:
        px = 1436 - x * 530
        py = 998 - (y + .55) * 530
        # Shoulder artwork converges toward the rear collar on the source.
        px = np.clip(px, 1263, 1611)
        py = np.clip(py, 410, 982)
    else:
        px = np.clip(927 + x * 530, 754, 1102)
        hem_edge = 760 + 12 * max(0, 1 - (x / .34) ** 2)
        py = np.clip(794 - (y + .55) * 540, 222, hem_edge)
    return [px / 1792, py / 1396]


def body(t, s, back=False):
    theta = -math.pi / 2 + s * math.pi + (math.pi if back else 0)
    y = -.55 + 1.065 * t
    radius_x = np.interp(y, [-.55, -.3, .08, .29, .41, .47, .49, .515],
                         [.339, .321, .32, .341, .333, .32, .21, .091])
    radius_z = np.interp(y, [-.55, -.25, .08, .29, .455, .515],
                         [.142, .136, .151, .157, .109, .079])
    x = radius_x * math.sin(theta)
    z = radius_z * math.cos(theta)
    front = max(0, math.cos(theta))
    shoulder = max(0, (t - .85) / .15)
    # A real opening: front neckline drops into the supplied V shape.
    y -= .142 * front ** 6 * shoulder ** 3
    # Broad, restrained cloth folds, strongest near side seams and the hem.
    edge = abs(math.sin(theta)) ** 3
    hem = (1 - t) ** 2
    fold = (.011 * math.sin(28 * x + 3 * y)
            + .004 * math.sin(48 * x - 9 * y)) * (.3 + hem + .4 * edge)
    fold += .009 * math.sin(11 * theta + 12 * y) * edge
    z += fold * math.cos(theta)
    x += .008 * math.sin(7 * y + 4 * theta) * hem
    y += .009 * math.sin(3 * theta + .4) * (1 - t) ** 6
    return [x, y, z], torso_uv(x, y, back)


surface(110, 90, body)
surface(110, 90, lambda t, s: body(t, s, True))


def sleeve(side, back=False):
    def point(t, s):
        theta = -math.pi / 2 + s * math.pi + (math.pi if back else 0)
        # Cylindrical sleeves with thickness and open cuffs.
        center = np.array([side * (.22 + .31 * t), .385 - .155 * t, 0])
        across = np.array([side * .447, .894, 0])
        radius = .104 - .019 * t
        radial = radius * math.sin(theta)
        p = center + across * radial
        p[2] = (.113 - .020 * t) * math.cos(theta)
        p[2] += .003 * math.sin(19 * t + 3 * theta) * math.cos(theta)
        q = (1 - math.sin(theta)) / 2
        # Bilinear mapping onto the corresponding sleeve on the exact sheet.
        if side > 0:
            upper0, lower0 = np.array([1003, 226]), np.array([1103, 397])
            upper1, lower1 = np.array([1215, 325]), np.array([1187, 420])
        else:
            upper0, lower0 = np.array([850, 226]), np.array([752, 397])
            upper1, lower1 = np.array([641, 325]), np.array([667, 420])
        source = (1 - q) * ((1 - t) * upper0 + t * upper1) + q * ((1 - t) * lower0 + t * lower1)
        if back:
            source[0] = 1436 - (source[0] - 927)
            source[1] = 402 + (source[1] - 211) * 1.12
        return p, [source[0] / 1792, source[1] / 1396]
    return point


for side in [-1, 1]:
    for back in [False, True]:
        surface(42, 48, sleeve(side, back))


def collar(t, s):
    # Open-front fold-over collar, with a raised neck stand and pointed leaves.
    theta = .32 + s * (math.tau - .64)
    front = max(0, math.cos(theta))
    if t < .32:
        f = t / .32
        rx = .091 + .007 * f
        rz = .079 + .007 * f
        y = .513 + .028 * f
    else:
        f = (t - .32) / .68
        rx = .098 + .058 * f
        rz = .086 + .057 * f
        y = .541 - .082 * f - .052 * front ** 3 * f
    return [rx * math.sin(theta), y, rz * math.cos(theta)], [0, 0]


surface(20, 110, collar, 1, False)

# The white V insert visible on the supplied front illustration.
v = [[-.085, .509, .085], [.085, .509, .085], [0, .373, .141]]
f = [0, 2, 1]
parts.append((v, [[0, 0]] * 3, f, normals(v, f), 1))

# Export a self-contained glTF 2.0 asset, with the untouched source JPG embedded.
blob = bytearray()
views, accessors = [], []


def add(data, target=None):
    blob.extend(b'\0' * ((-len(blob)) % 4))
    entry = {'buffer': 0, 'byteOffset': len(blob), 'byteLength': len(data)}
    if target:
        entry['target'] = target
    views.append(entry)
    blob.extend(data)
    return len(views) - 1


def accessor(values, kind):
    array = np.asarray(values, dtype='<u4' if kind == 'SCALAR' else '<f4')
    entry = {'bufferView': add(array.tobytes(), 34963 if kind == 'SCALAR' else 34962),
             'componentType': 5125 if kind == 'SCALAR' else 5126,
             'count': len(array), 'type': kind}
    if kind == 'VEC3':
        entry.update(min=array.min(axis=0).tolist(), max=array.max(axis=0).tolist())
    accessors.append(entry)
    return len(accessors) - 1


primitives = []
for p, uv, faces, n, material in parts:
    primitives.append({'attributes': {'POSITION': accessor(p, 'VEC3'),
                                      'NORMAL': accessor(n, 'VEC3'),
                                      'TEXCOORD_0': accessor(uv, 'VEC2')},
                       'indices': accessor(faces, 'SCALAR'), 'material': material})
image_view = add((ROOT / 'design-reference.jpg').read_bytes())
doc = {'asset': {'version': '2.0', 'generator': 'NOIR garment reconstruction v2',
                 'extras': {'status': 'Full-volume review reconstruction. Construction inferred from flat artwork.'}},
       'scene': 0, 'scenes': [{'nodes': [0]}],
       'nodes': [{'mesh': 0, 'name': 'Budak Gang — volume reconstruction'}],
       'meshes': [{'primitives': primitives}],
       'materials': [
           {'name': 'Supplied print artwork', 'pbrMetallicRoughness': {'baseColorTexture': {'index': 0}, 'metallicFactor': 0, 'roughnessFactor': .87}},
           {'name': 'White fold-over collar', 'doubleSided': True, 'pbrMetallicRoughness': {'baseColorFactor': [.96, .96, .94, 1], 'metallicFactor': 0, 'roughnessFactor': .9}},
           {'name': 'Inferred interior cloth', 'pbrMetallicRoughness': {'baseColorFactor': [.32, .028, .033, 1], 'metallicFactor': 0, 'roughnessFactor': 1}}],
       'textures': [{'source': 0, 'sampler': 0}],
       'samplers': [{'magFilter': 9729, 'minFilter': 9987, 'wrapS': 33071, 'wrapT': 33071}],
       'images': [{'bufferView': image_view, 'mimeType': 'image/jpeg'}],
       'accessors': accessors, 'bufferViews': views, 'buffers': [{'byteLength': len(blob)}]}
data = json.dumps(doc, separators=(',', ':')).encode()
data += b' ' * ((-len(data)) % 4)
blob.extend(b'\0' * ((-len(blob)) % 4))
output = struct.pack('<III', 0x46546c67, 2, 28 + len(data) + len(blob))
output += struct.pack('<II', len(data), 0x4e4f534a) + data
output += struct.pack('<II', len(blob), 0x004e4942) + blob
target = ROOT / 'noir-jersey-v2.glb'
target.write_bytes(output)
print(f'{target}: {len(output) / 1024 / 1024:.2f} MB; {len(parts)} cloth surfaces')
