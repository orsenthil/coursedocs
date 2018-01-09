OpenCV
======

http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_core/py_basic_ops/py_basic_ops.html


.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4zHbI-fFIlI" frameborder="0" allowfullscreen></iframe>

Blur / Noise Without Noise
--------------------------

::

    Blur/Smooth Without Noise?
    Right now for HoughCircles, I'm doing:

    1. convert image to grayscale
    2. get edge image with canny
    3. pass edge image to houghcircles

    For HoughLines:

    0 (if needed) use cv2.inRange to get color masks
    1. get edge image with canny
    2. pass edge image to houghlines

    My understanding before was that smoothing an image helps when there's Gaussian noise to get rid of high frequency pixels. Maybe I'm confusing myself...but should we be smoothing regardless of whether there's noise or not? If so, does the smoothing come after converting to gray scale or using color masks? Or after canny?

    Been working on this pset for close to 20 hours now and still stuck on part 4 so any help to clear this up would be awesome!

::

    I used a Gaussian filter to smooth the image before manipulating it in any other way -
    I pass the smoothed image into my other functions to mask and get houghlines, etc.
    It seems to be working pretty well.


