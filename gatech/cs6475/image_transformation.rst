Image Transformation
====================

Image Transformations
---------------------

Image transformations change the **domain** (pixel coordinates) rather than the **range** (pixel intensities). Transformations include translation, rotation, scaling, affine warps, and projective warps. See the detailed notes in the companion section for mathematical foundations, homogeneous coordinates, and code demos.

Image Morphing
--------------

**Image morphing** combines warping (geometric transformation) with cross-dissolving (intensity blending) to create smooth transitions between two images. Key steps:

- Define corresponding feature points/lines in source and target images
- Compute intermediate warps for each frame
- Cross-dissolve pixel intensities at each intermediate step

Panorama
--------

**Panorama stitching** aligns and blends multiple overlapping images into a single wide field-of-view composite:

- Detect and match features across image pairs
- Estimate homography (projective transformation) between images
- Warp images into a common coordinate frame
- Blend seams to produce the final panorama

High Dynamic Range (HDR)
------------------------

**HDR imaging** captures and merges multiple exposures of the same scene to recover the full range of irradiance values:

- Capture bracketed exposures (short → long)
- Estimate camera response curve
- Reconstruct radiance map
- Apply **tone mapping** to display on standard monitors

Stereo
------

**Stereo vision** uses two images from slightly different viewpoints to estimate depth:

- Find corresponding points between left and right images
- Compute **disparity** (pixel offset) — inversely proportional to depth
- Generate a **depth map** from disparity values

Photosynth
----------

**Photosynth** (Microsoft) reconstructs 3D scenes from large collections of unstructured photographs using structure-from-motion techniques.

Extrinsic Camera Parameters
---------------------------

**Extrinsic parameters** describe the camera's position and orientation in world coordinates:

- **Rotation matrix** R (3×3): camera orientation
- **Translation vector** t (3×1): camera position
- Combined as a 3×4 matrix [R | t]

Intrinsic Camera Parameters
----------------------------

**Intrinsic parameters** describe the camera's internal geometry:

- **Focal length** (fx, fy)
- **Principal point** (cx, cy) — where optical axis meets image plane
- **Skew coefficient**
- Encoded in the 3×3 **camera matrix** K

Camera Calibration
------------------

**Camera calibration** recovers intrinsic and extrinsic parameters from images of known calibration targets (e.g., checkerboard patterns) using techniques like Zhang's method.
