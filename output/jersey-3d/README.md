# NOIR jersey — 3D review study

## October 12 reconstruction

`noir-jersey-v2.glb` is the full-volume reconstruction currently used by the
homepage. Its editable source is `build_model_v2.py`. It uses curved torso
surfaces, cylindrical open sleeves, interior cloth surfaces and an open-front
fold-over collar. Front and rear UV surfaces are split to avoid pulling the
sheet background across the side seam. The source artwork is embedded unchanged.

This remains an artwork-based reconstruction. It is not a garment scan or a
measured production replica. Sleeve/body intersections, inferred collar
construction and cloth drape still need comparison with a physical garment.
The raster source limits fine print detail; no new sponsors or logos are added.
The shader's fine weave is an illustrative material response, not a measured
fabric specification. The previous v1 asset is preserved for comparison.

Rebuild with `python3 output/jersey-3d/build_model_v2.py`, then copy the GLB to
`public/models/noir-jersey-v2.glb`.

Open the local preview at http://127.0.0.1:8766 while its server is running.
Drag horizontally, use the rotation slider, or select Front / Side / Back.
The canvas supports arrow keys and Home. Rendering happens only on interaction
or resize; there is no automatic rotation and no external JavaScript dependency.

## Files

- `noir-jersey-v1.glb`: portable glTF 2.0 model, including its JPEG texture.
- `design-reference.jpg`: unchanged copy of the supplied design sheet.
- `index.html`: standalone WebGL 2 review viewer, independent of Astro.
- `build_model.py`: editable mesh and UV construction script (numpy/scipy).

## Scope and limitations

This is actual rotatable geometry, not an image flip or a rotation video.
It is an initial garment study, not a finished photorealistic production asset.
The front and rear artwork is sampled from the original sheet, not redrawn by AI.
The source is a flattened illustration with outlines and baked shading; those
remain visible. Small printed details are limited by its resolution.

Body volume, sleeve openings, collar shape, interior color and drape are inferred.
Fine seam construction, fabric normal maps and physically simulated cloth have
not been established. The current collar and sleeve transition need further
refinement to match the approved static visual. A production-quality finish
would benefit from clean print artwork and side/collar photographs or an actual
garment pattern. No production dimensions or fabric properties are asserted.

No homepage source, Astro version or dependencies were changed. Integrating this
study into What We Make requires the user's separate section review.

## Rebuild / preview

Run `python3 output/jersey-3d/build_model.py` from the project root.
Run `python3 -m http.server 8766 --bind 127.0.0.1 --directory output/jersey-3d`
from the project root to serve the preview.
