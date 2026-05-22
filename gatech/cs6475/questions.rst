Questions and Concepts
======================

Epsilon to Coded Photography
-----------------------------

**Computational photography** extends traditional cameras through computation, smart lights, and novel optics.

**Epsilon photography** synthesizes omnipictures via the **multiple capture, single image (MCSI)** paradigm — scene properties are encoded across a few photographs with slightly varied camera parameters.

**Coded photography** encodes scene information through modulated optics (aperture, shutter, illumination), then computationally decodes richer representations. Key foundations:

- Fourier transform and Fourier optics
- Optical heterodyning
- Helmholtz reciprocity: https://en.wikipedia.org/wiki/Helmholtz_reciprocity

Light Field
-----------

The **light field** describes the amount of light traveling in every direction through every point in space.

The **plenoptic illumination function** expresses the image of a scene from any viewing position, angle, and time. Since rays are parameterized by three spatial coordinates :math:`(x, y, z)` and two angles :math:`(\theta, \phi)`, it is a **five-dimensional function**.

Computational Illumination
--------------------------

Computational illumination asks: *what spatio-temporal modulations of light best reveal the visually important contents of a scene?*

- Changing color filters, tunable wavelength filters, or diffraction gratings
- Better lighting control during capture enables richer scene representations
- Reference: https://en.wikipedia.org/wiki/Harold_Eugene_Edgerton

**Epsilon photography approach**: Each camera setting records partial scene information; the final image is reconstructed by computationally merging multiple observations, combining the best features from each.
