Fourier Transform
=================

Images are samples of different intensities that can be represented in the **frequency domain**. Frequency representations enable powerful analysis and manipulation techniques.

Lesson Objectives
-----------------

- Using sines and cosines to reconstruct a signal
- The Fourier Transform and its properties
- Frequency domain representation of signals and images
- Three properties of convolution (commutativity, associativity, distributivity)

Fourier Transform
-----------------

The **Fourier Transform** decomposes a signal (or image) into a sum of sinusoidal components at different frequencies, amplitudes, and phases. This reveals which frequencies dominate the signal.

- **Low frequencies** correspond to smooth, slowly varying regions
- **High frequencies** correspond to edges and fine detail
- Filtering in the frequency domain (e.g., low-pass, high-pass) is equivalent to convolution in the spatial domain

Blending
--------

Frequency-domain analysis informs blending strategies — e.g., blending low frequencies from one image with high frequencies from another (hybrid images).

Pyramids
--------

**Gaussian and Laplacian pyramids** provide a multi-scale frequency decomposition useful for blending, compression, and analysis.

Cuts
----

**Graph cuts** and **min-cut/max-flow** algorithms find optimal seams for compositing images.

Features
--------

Feature detection identifies distinctive points in images for matching, alignment, and recognition.

Feature Detection and Matching
------------------------------

Techniques for detecting and matching features across images:

- **Harris corner detector**: Finds points with large intensity variation in multiple directions
- **SIFT** (Scale-Invariant Feature Transform): Detects and describes features invariant to scale and rotation
- **Feature matching**: Comparing descriptors between images to find correspondences
