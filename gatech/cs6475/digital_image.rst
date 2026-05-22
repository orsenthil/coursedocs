Digital Image
=============

What is a Digital Image?
------------------------

A digital image is a 2D function :math:`I(x, y)` mapping pixel coordinates to intensity values, making images computable entities that can be stored, processed, and analyzed as matrices.

Digital Image Formats
~~~~~~~~~~~~~~~~~~~~~

**Raster image formats** store a grid of colored dots (pixels). The number of bits per pixel determines color depth:

- **1 bpp**: 2 colors (binary — black or white)
- **4 bpp**: 16 colors
- **8 bpp**: 256 colors
- **24 bpp**: 8 bits per channel (RGB) — 16,777,216 colors
- **32 bpp**: 24-bit color + 8-bit alpha channel

Common formats: GIF, JPG, PPM, TIF, BMP, camera RAW.

Tools: OpenCV/Python, MATLAB/Octave, Processing.org

Point Processes
---------------

**Point processes** operate on individual pixels independently — the output at :math:`(x, y)` depends only on the input at :math:`(x, y)`.

Operations on Images
~~~~~~~~~~~~~~~~~~~~

- **Add/Subtract**: Combine or difference two images pixel-wise
- **Alpha blending**: Weighted combination of images using transparency parameter :math:`\alpha \in [0, 1]`

  - :math:`\alpha = 0` → invisible, :math:`\alpha = 1` → fully visible
  - RGB becomes :math:`\alpha` RGB (premultiplied alpha)
  - Blend: :math:`I_{out} = \alpha \cdot I_A + (1 - \alpha) \cdot I_B`

- **Image histograms**: Distribution of pixel intensity values; useful for contrast analysis and equalization

Blending Modes
--------------

Blending modes define how two layers of pixels are combined:

**Arithmetic modes**:

- **Average**: :math:`f(a, b) = (a + b) / 2`
- **Normal**: :math:`f(a, b) = b`
- **Addition**: Tends to produce whites (overexposure)
- **Subtraction**: Tends to produce blacks (underexposure)
- **Difference**: Subtract with scaling
- **Divide**: Brightens photos
- **Darken**: :math:`f(a, b) = \min(a, b)` per channel
- **Lighten**: :math:`f(a, b) = \max(a, b)` per channel

**Advanced modes**:

- **Multiply**: Darkens — :math:`f(a, b) = a \cdot b`
- **Screen**: Brightens — :math:`f(a, b) = 1 - (1 - a)(1 - b)`

Reference: https://en.wikipedia.org/wiki/Blend_modes

Smoothing
---------

Smoothing reduces noise by averaging pixel values over a neighborhood.

**Box filter (averaging)**: Replaces each pixel with the uniform average of its kernel neighborhood (e.g., 21×21).

**Gaussian filter**: Weights neighbors by a Gaussian distribution — closer pixels contribute more. Produces smoother results than box filtering.

**Median filtering**: A non-linear operation that replaces each pixel with the **median** of all pixels in the kernel area.

- Reduces noise effectively
- **Preserves edges** (sharp lines) — unlike averaging filters which blur edges
- Main idea: use median instead of mean

Convolution and Cross-Correlation
----------------------------------

**Cross-correlation**: Sliding dot product of a kernel :math:`h` over an image :math:`F`:

.. math::

   G[i, j] = \sum_{u=-k}^{k} \sum_{v=-k}^{k} h[u, v] \cdot F[i + u, j + v]

Denoted :math:`G = h \otimes F`.

- Replaces each pixel with a **linear combination** of its neighbors
- The kernel :math:`h[u, v]` specifies the weights

**Convolution**: Same as cross-correlation but with a **flipped kernel**. For symmetric kernels, cross-correlation and convolution produce identical results.

**Common filters**:

- **Box filter**: Uniform weights (e.g., 21×21) — averaging
- **Gaussian filter**: Weights follow normal distribution — smoother falloff

Gradients and Edge Detection
-----------------------------

**Edges** are locations of rapid change in the image intensity function :math:`F(x, y)`. They appear as ridges in the 3D height map of an image.

Discontinuities arise from changes in:

- Surface normal
- Depth
- Surface color
- Illumination

**Edge detection approach**:

1. Look for neighborhoods with strong signs of change
2. Considerations: neighborhood size, change metric, threshold
3. Compute **gradients** (discrete derivatives) using kernels

**Gradient kernels** (operators for computing discrete derivatives):

- **Prewitt**: Equal-weight gradient approximation
- **Sobel**: Weighted gradient approximation (emphasizes center row/column)
- **Roberts**: 2×2 diagonal difference operator

**Canny Edge Detector**: The standard multi-stage edge detection algorithm:

1. Smooth with Gaussian filter
2. Compute gradient magnitude and direction
3. Non-maximum suppression (thin edges)
4. Hysteresis thresholding (strong/weak edge linking)
