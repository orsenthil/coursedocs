Light Field
===========

Light Field
-----------

The **light field** is a function describing the amount of light traveling in every direction through every point in space. It is a fundamental concept in computational photography.

- The **plenoptic function** :math:`P(\theta, \phi, \lambda, t, V_x, V_y, V_z)` captures all possible views of a scene (position, direction, wavelength, time).
- For static scenes, rays can be parameterized by **two planes** (4D representation): :math:`L(u, v, s, t)`.
- **Light field cameras** (e.g., Lytro) capture the 4D light field in a single exposure using a microlens array, enabling post-capture refocusing and depth estimation.

Projector-Camera Systems
-------------------------

**Projector-camera (pro-cam) systems** combine a projector and camera to enable:

- Scene geometry recovery via structured light
- Radiometric compensation (adapting projected images to non-white/non-flat surfaces)
- Augmented reality on arbitrary surfaces
- Dual photography (reconstructing the projector's view using Helmholtz reciprocity)

Coded Photography
-----------------

**Coded photography** modifies camera parameters (aperture, exposure, sensor) during capture to encode additional scene information:

- **Coded aperture**: Non-standard aperture patterns that enable depth estimation and deblurring from a single image
- **Flutter shutter**: Temporally coded exposure that preserves high-frequency information in motion-blurred images, enabling deblurring
- **Coded illumination**: Spatially or temporally modulated lighting to separate direct and indirect illumination
