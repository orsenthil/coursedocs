Basics for Image Processing
===========================

Kernels
-------

A **kernel** (filter mask) is a fixed-size array of numerical coefficients with an anchor point, typically at the center. The kernel is convolved with the image to produce filtered output.

   :align: center
   :height: 300
   :width: 450

Gaussian Pyramids
-----------------

A **Gaussian pyramid** is built by repeatedly blurring (Gaussian average) and downsampling an image. Each level contains a local average corresponding to a pixel neighborhood at the level below. Used extensively in **texture synthesis** and multi-scale analysis.

Laplacian Pyramids
------------------

A **Laplacian pyramid** stores the **difference** between successive Gaussian pyramid levels rather than the blurred images themselves. Only the smallest (coarsest) level is stored directly — all higher levels are difference images that enable reconstruction of the full-resolution image. Used in **image compression** and **blending** (e.g., Laplacian pyramid blending for seamless composites).

Sobel Operator
--------------

The Sobel operator computes image gradients by convolving with directional derivative kernels. It is commonly used in edge detection.

.. math::

   \min _ { s ^ { x } ,s ^ { y } ,\alpha } \sum _ { i = 1} ^ { k } E \left( \alpha _ { i } \mathbf { s } _ { \mathbf { i } } ^ { \mathbf { X } } + \left( 1- \alpha _ { i } \right) \mathbf { s } _ { \dot { i } } ^ { y } \right)
