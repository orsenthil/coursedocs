Image Transformations
=====================

Image Filtering vs Image Warping
---------------------------------

Two fundamental ways to transform an image:

- **Image filtering**: changes the *range* (pixel intensity values). Output ``g(x,y) = h(f(x,y))``.
- **Image warping**: changes the *domain* (pixel coordinates/positions). Output ``g(x',y') = f(T(x,y))``.

Filtering modifies what each pixel contains; warping modifies where each pixel is located.

Parametric Global Warping
-------------------------

Goal: find a single transformation function ``T`` with parameters that maps every point
``p = (x, y)`` to ``p' = (x', y')`` uniformly across the entire image.

Matrix representation:

.. math::

   p' = M \cdot p

where ``M`` encodes all transformation parameters. For 2D transforms, ``M`` is initially
a 2x2 matrix applied to ``[x, y]^T`` to produce ``[x', y']^T``.

2D Scaling
~~~~~~~~~~

.. math::

   \begin{bmatrix} x' \\ y' \end{bmatrix} =
   \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}
   \begin{bmatrix} x \\ y \end{bmatrix}

- Uniform scaling: ``s_x = s_y``
- Non-uniform scaling changes aspect ratio

2D Rotation
~~~~~~~~~~~

.. math::

   \begin{bmatrix} x' \\ y' \end{bmatrix} =
   \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
   \begin{bmatrix} x \\ y \end{bmatrix}

Derived from trigonometric identities for rotating a point by angle ``theta``.

2D Shear
~~~~~~~~

.. math::

   M = \begin{bmatrix} 1 & sh_x \\ sh_y & 1 \end{bmatrix}

Off-diagonal terms produce shear in x and y directions.

Mirroring
~~~~~~~~~

- ``diag(-1, 1)``: mirror about y-axis (flip horizontal)
- ``diag(1, -1)``: mirror about x-axis (flip vertical)
- ``diag(-1, -1)``: mirror about origin (flip both)

Properties of 2D Linear Transformations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Origin maps to origin (no translation possible)
- Lines map to lines
- Parallel lines remain parallel
- Ratios are preserved

Homogeneous Coordinates
-----------------------

The 2x2 matrix cannot represent translation (which requires addition, not multiplication).
Solution: extend to homogeneous coordinates.

Convert 2D point ``(x, y)`` to 3-vector ``(x, y, w)`` where:

- The 2D point is recovered as ``(x/w, y/w)``
- Typically ``w = 1``, so ``(x, y, 1)``
- ``w = 0`` represents a point at infinity
- ``(0, 0, 0)`` is undefined

This allows all transformations (including translation) to be expressed as a single
3x3 matrix multiplication.

2D Transformations in Homogeneous Coordinates
---------------------------------------------

Translation
~~~~~~~~~~~

.. math::

   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

Scale
~~~~~

.. math::

   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

Rotation
~~~~~~~~

.. math::

   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

Shear
~~~~~

.. math::

   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix} 1 & sh_x & 0 \\ sh_y & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

Composite transformations are achieved by multiplying matrices (translation + rotation + shear, etc.).

Affine Transformations
----------------------

Combines linear transformations (rotation, scale, shear) with translation.

.. math::

   \begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} =
   \begin{bmatrix} a & b & c \\ d & e & f \\ 0 & 0 & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

- **DOF**: 6 (parameters a, b, c, d, e, f)
- **Point correspondences needed**: 3
- **Properties preserved**: lines map to lines, parallel lines remain parallel
- **Not preserved**: origin does not necessarily map to origin

Projective Transformations
--------------------------

Combines affine transformation with a projective warp.

.. math::

   \begin{bmatrix} x' \\ y' \\ w' \end{bmatrix} =
   \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & 1 \end{bmatrix}
   \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}

- **DOF**: 8 (bottom-right element is fixed at 1)
- **Point correspondences needed**: 4
- **Properties preserved**: straight lines remain straight
- **Not preserved**: parallelism, ratios

Summary of Transformation Types
--------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 10 15 30

   * - Transformation
     - DOF
     - Correspondences
     - Preserved
   * - Translation
     - 2
     - 1
     - Orientation
   * - Rigid (Euclidean)
     - 3
     - 2
     - Lengths, angles
   * - Similarity
     - 4
     - 2
     - Angles
   * - Affine
     - 6
     - 3
     - Parallelism, straight lines
   * - Projective
     - 8
     - 4
     - Straight lines only

Code Demos
----------

Translation
~~~~~~~~~~~

Use ``cv2.warpAffine`` with a 2x3 transformation matrix::

    import cv2
    import numpy as np

    img = cv2.imread('image.png')
    rows, cols = img.shape[:2]

    # Translation matrix: shift by tx=100, ty=50
    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    translated = cv2.warpAffine(img, M, (cols, rows))

Rotation
~~~~~~~~

Use ``cv2.getRotationMatrix2D`` to build the rotation matrix::

    # Rotate 45 degrees around origin (0,0)
    M = cv2.getRotationMatrix2D((0, 0), 45, 1)
    rotated = cv2.warpAffine(img, M, (cols, rows))

    # Rotate -45 degrees around image center
    center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, -45, 1)
    rotated_center = cv2.warpAffine(img, M, (cols, rows))

Scale and Shear
~~~~~~~~~~~~~~~

::

    # Scale by 1.5x in both directions
    scaled = cv2.resize(img, None, fx=1.5, fy=1.5)

    # Horizontal shear (off-diagonal term)
    M = np.float32([[1, 0.5, 0],
                    [0, 1,   0]])
    sheared = cv2.warpAffine(img, M, (cols, rows))

Affine Warp
~~~~~~~~~~~

Compute from 3 point correspondences::

    pts1 = np.float32([[p1], [p2], [p3]])
    pts2 = np.float32([[p1'], [p2'], [p3']])

    M = cv2.getAffineTransform(pts1, pts2)
    warped = cv2.warpAffine(img, M, (cols, rows))

Perspective Warp
~~~~~~~~~~~~~~~~

Compute from 4 point correspondences::

    pts1 = np.float32([[p1], [p2], [p3], [p4]])
    pts2 = np.float32([[p1'], [p2'], [p3'], [p4']])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(img, M, (cols, rows))

Forward vs Inverse Warping
--------------------------

Forward Warping
~~~~~~~~~~~~~~~

- For each pixel in source ``f(x,y)``, compute destination ``T(x,y)`` in output.
- Problem: destination may land between pixel locations.
- Solution: distribute (splat) color among neighboring pixels.
- Risk: **holes** — some output pixels may never be mapped to.

Inverse Warping
~~~~~~~~~~~~~~~

- For each pixel in output, compute source location ``T^{-1}(x',y')`` in input.
- Problem: source location may land between pixel locations.
- Solution: **interpolate** color from neighboring source pixels.
- Advantage: no holes in output (every output pixel is filled).
- Requirement: need an invertible warp function ``T^{-1}``.

Inverse warping is generally preferred because it eliminates holes. Invertibility is
straightforward for rigid transforms (rotation, translation, scale) but becomes harder
for non-global or complex warps.

Reference
---------

Szeliski, *Computer Vision: Algorithms and Applications*, Chapter 2.
