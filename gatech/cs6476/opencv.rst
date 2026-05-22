OpenCV
======

* Reference: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4zHbI-fFIlI" frameborder="0" allowfullscreen></iframe>

Smoothing Before Edge Detection
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
