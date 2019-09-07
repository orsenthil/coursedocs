Questions
=========

* What is exposure stacking?


Computational Photography: Epsilon to Coded Photography
-------------------------------------------------------

Computational photography includes use of "Smart Lights" to escape the limitations of traditional camera.

Epsilon photography is concerned with synthesizing omnipictures and proceeds by multiple capture single image paradigm (MCSI).

The scene properties are encoded in few photographs.

Fourier transform
Fourier optics
Optical heterodyning.

Light Field

The light field is a function that describes the amount of light traveling in every direction through every point in space.

plenoptic function.

The plenoptic illumination function is an idealized function used in computer vision and computer graphics to express the image of a scene from any possible viewing position at any viewing angle at any point in time.

Since rays in space can be parametrized by three spatial coordinates, x, y and z and two angles :math:`\theta` and :math:`\sigma` it is a five dimensional function.

Show the lighting and effect
----------------------------

Capturing the visually meaningful changes from the light leaving the scene.

* Single Object Change.
* Richer Visual Experience.
* Field of View.
* Close Depth of Field for all objects.
* Records the moment.
* Interactive Display.

* Fraction of the Light field of the scene.
* Fusion of time-lapsed events.

* Not a fluttering shutter.

* Image Stabilizing.

Computational illumination
--------------------------

What sorts of spatio-temporal modulations for light might better reveal the visually important contents of a scene?

https://en.wikipedia.org/wiki/Harold_Eugene_Edgerton


* Spatio-temporal modulations for light might better reveal the visually important

* spatio-temporal modulators and optics

https://en.wikipedia.org/wiki/Helmholtz_reciprocity

changing color filters in front of the camera, using tunable wavelength filters or using diffraction gratings


better lighting control during cap- ture allows one to build richer representations of photographed scenes.

Camera Parameter - Instant of Capture - Change.

Each setting allows recording of partial information about the scene and the final image is reconstructed from these multiple observations.

multiple film-style photos computationally merged for a scene description.

The merged photo contains the best features from all of them.

Novel illumuniation


Capturing a rubik's cube solution, with changes of instance of capture.
We merge the photos to create rich time-lapse events of the solution.
To add some more color, the time-lapse is presented with focus on two toys near the Rubiks cube.

Digital Image Formats
---------------------

* GIF, JPG, PPM, TIF, BMP
* Raw Format.
* OpenCV / Python
* opencv.org, python.org
* Matlab / Octave
* Processing.org
* Exercises: Read and write images.
* Image compression information.
* Metadata about pictures (Exchangeable Image file format - EXIF "etc").

Digital Image - Processing and Filtering
----------------------------------------

* Point-process computations.
* Add/Subtract Images.
* alpha-blending and its applications.
* Image Histograms.
* I(x, y)

Point-process: Pixel / Point Arithmetic
---------------------------------------

* 0-255
* 0.34 * CD + 0.34 * AE + 0.34 * LD =
* Transparency (Conversely, Opacity).
* Usually represented as :math:`\alpha`
* :math:`\alpha` varies from 0 to 1. (0 = invisible, 1 = fully visible).
* RGB :math:`\righarrow` :math:`\alpha` RGB
* Point process computations on Images to Add and Subtract images.
* Showed an example of :math:`\alpha` blending commonly used in Image processing.
* Image Histogram in Image processing.


Image Processing, Filtering via Convolution and Correlation
-----------------------------------------------------------

* A Real life example of point arithmetic
* Variety of Blending modes built on concept of point processes.
* average = fblend(a, b) = (a + b) / 2
* normal = fblend(a, b) = b

Arithmetic Blend modes
----------------------

* Divide (brightens photos)
* Addition (too many whites)
* Subtract (too many blacks)
* Difference (subtract with scaling)
* Darken fblend(a, b) = min(a, b) for RGB
* Lighten: blend(a, b) = max(a, b) for RGB

Advanced Modes
--------------

* Multiply
    * Darker fblend(a, b) = ab
* Screen
    * brighter fblend(a, b) = 1 - (1 - a)(1 - b)

Summary
-------

* Introduced Pixel / Layer Blending
* Explained variety of blending approaches
* Showed why some of the videos look ODD

Lesson Objectives
-----------------

* Smooth an image over a neighborhood of pixels.
* Media filtering as a special non-linear filtering and smoothing approach.
* How to Smooth a Signal?

A mathematical representation for smoothing
-------------------------------------------

* Cross-correlation or x-correlation.

Box Filter (Averaging) for Smoothing
------------------------------------

* Box / Average Filter - 21 x 21

Special Case: Median Filtering
------------------------------

Median filtering is a non-linear operation often used in image processing.

* Reduce noise, but
* Preserves Edges (Sharp Lines!)

Main Idea: Use median of all pixels in the kernel area, instead of mean.

Average filter (11 x 11)
Median filter (11 x 11)

* Image smoothing
* Applying a kernel to smooth an image.
* Averaging and median filtering.

Next Class
----------

Cross Correlation and Convolution.

1. Cross-Correlation.
2. Convolution
3. Difference between Cross-Correlation and Convolution.
4. Properties of these methods.

* In signal processing, cross-correlation is a measure of similarity of two waveforms as a function of a time-lag applied to one of them.

* Sliding dot product or sliding inner-product of two different matrices.

Cross-Correlation Method
------------------------

    G[i, j] = :math:\sum_{u=-k}^{k}\sum_{v=-k}^k h[u, v] F[i + u, j + v]

Denoted by


    G = h :math:\bigotimes F

* Filtering an image.
* Replace each pixel with a linear combination of its neighbors.

* Filter "kernel" or "mask"
* h[u, v] is a prescription for weights in the linear combination.

Example: Box Filter
-------------------

Box/ Average Filter

* Size 21 x 21
* Values: Uniform

Example: Gaussian Filter
------------------------

Gaussian Filter

* Size: 21 x 21
* Values: Gaussian or Normal Distribution.

Using Gaussian Filters for Smoothing
------------------------------------


Convolution Method
------------------

* Convolution is a mathematical operation on two functions F and h


Linear Filters
--------------

* Original 64 x 64
* Cross-Correlation
* Convolution
* Differences between Cross-correlation and convolution.


Image Analysis and Edge Detection
---------------------------------

* Image Variance
* Convolution and Cross Correlation.
* Using Filters to Find Features
* Map raw pixels to an intermediate representation.
* Reduce amount of data, preserve useful information.


Good features to match between images
-------------------------------------

Features

* Water bottle
* Parts of an image that encode it in a compact form.

Edges

What kind of discontinuities are in a scene?

* Surface Normal
* Depth
* Surface Color
* Illumination.

Images as Functions F(x, y)
---------------------------

Edges appear as ridges in the 3d height map of an image.

Edge Detection
--------------

Basic Idea

* Look for a neighborhood with strong signs of change.

Issues to consider.

* Size of the neighborhood? K=1
* What metrics represent a "change"?
* Threshold

Derivatives of F(x, y) to get Edges
-----------------------------------

Test Image

* An Edge where there is a rapid change in the image intensity function.

Edge Detection
--------------

* Feature Detection.
* Reliable way to extract information from images.
* Compute Edges.
* Derivatives using kernels and neighborhood operations.
* Three (3) methods for computing edges using kernels
* Image noise can complicate the computation of gradients.
* The Canny Edge Detector.

Computing Discrete Gradients
----------------------------

An "operator" (mask / kernel) that effectively computes discrete derivative values with
cross-correlation (using finite differences).

Various Kernels for Computing Gradients
---------------------------------------

Prewitt

Sobel

Roberts

Canny Edge Detector
-------------------


