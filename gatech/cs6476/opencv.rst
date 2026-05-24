OpenCV
======

* Reference

---------------------------------

A common pipeline for feature detection:

**HoughCircles pipeline**:

1. Convert image to grayscale
2. Get edge image with Canny
3. Pass edge image to ``cv2.HoughCircles``

**HoughLines pipeline**:

1. (Optional) Use ``cv2.inRange`` for color masks
2. Get edge image with Canny
3. Pass edge image to ``cv2.HoughLines``

**When to smooth**: Apply Gaussian smoothing *before* edge detection (before Canny), regardless of whether visible noise is present. Smoothing suppresses high-frequency pixel variations that produce spurious edges. Apply smoothing after grayscale conversion but before Canny.

.. code-block:: python

   smoothed = cv2.GaussianBlur(gray, (5, 5), 0)
   edges = cv2.Canny(smoothed, threshold1, threshold2)
