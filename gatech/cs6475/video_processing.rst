Video Processing
================

Video Processing Fundamentals
------------------------------

Video is a sequence of image frames over time — :math:`I(x, y, t)`. Video processing extends image processing to the temporal domain, enabling motion analysis, temporal filtering, and dynamic scene manipulation.

Video Textures
--------------

**Video textures** create infinitely looping video by finding visually similar frames and creating seamless transitions:

- Compute frame-to-frame similarity (e.g., sum of squared differences)
- Build a transition cost matrix
- Find low-cost transition points that allow seamless looping
- Randomly sample transitions to create non-repeating, infinite-length video

Video Stabilization
-------------------

**Video stabilization** removes unwanted camera shake while preserving intentional motion:

- Estimate frame-to-frame camera motion (translation, rotation, affine)
- Smooth the estimated motion trajectory (e.g., moving average, L1-optimal smoothing)
- Apply corrective warps to each frame to follow the smoothed trajectory
- Crop borders to remove artifacts from warping

Panoramic Video Textures
-------------------------

Combines panoramic stitching with video textures to create wide field-of-view looping video from panning camera footage.
