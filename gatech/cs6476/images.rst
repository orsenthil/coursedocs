Images
======

Reading and Displaying Images
-----------------------------

.. code-block:: python

   import numpy as np
   import cv2

   img = cv2.imread('messi5.jpg', 0)  # 0 = grayscale
   cv2.imshow('image', img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

- ``cv2.imread(path, flag)`` — reads an image; flag ``0`` for grayscale, ``1`` for color (BGR)
- ``cv2.imshow(window_name, img)`` — displays image in a window
- The **alpha channel** is a fourth channel (RGBA) representing transparency per pixel
