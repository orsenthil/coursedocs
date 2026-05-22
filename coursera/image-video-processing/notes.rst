Image Video Processing Notes
============================

JPEG Compression
----------------

The JPEG pipeline divides an image into **n×n subimages** (typically 8×8 blocks), applies a forward transform, quantizes the coefficients, and entropy-codes the result.

Color Space Conversion
~~~~~~~~~~~~~~~~~~~~~~

JPEG operates in **YCbCr** color space, not RGB. The Y channel carries luminance; Cb and Cr carry chrominance. JPEG exploits the human visual system's lower sensitivity to color detail by subsampling the chrominance channels.

Discrete Cosine Transform (DCT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **DCT** converts each block from the spatial domain to the frequency domain. It is preferred over the Fourier Transform because it produces real-valued coefficients and is invertible.

- The DCT basis function coefficient:

  .. math::

     \alpha(u) = \begin{cases} \sqrt{1/n} & u = 0 \\ \sqrt{2/n} & u \neq 0 \end{cases}

- The 2D transform produces coefficients :math:`T(u, v)` for each block.
- Applying many small DCTs (e.g., n=4 or n=8) is computationally cheaper than a single large DCT over the full image.
- The **Karhunen-Loève Transform** (KLT) is the theoretically optimal transform but is data-dependent; the DCT closely approximates KLT for natural images at much lower cost. See: https://en.wikipedia.org/wiki/Karhunen%E2%80%93Lo%C3%A8ve_theorem

Quantization
~~~~~~~~~~~~

**Quantization** maps the continuous-valued DCT coefficients to a finite set of discrete levels, introducing controlled loss. The **Max-Lloyd Optimal Quantizer** minimizes mean squared error for a given number of quantization levels.

Error Measurement
~~~~~~~~~~~~~~~~~

Compression quality is measured by **Mean Squared Error (MSE)**:

.. math::

   MSE = \frac{1}{N} \sum (\hat{F} - F)^2

where :math:`N` is the number of pixels, :math:`F` is the original, and :math:`\hat{F}` is the reconstructed image.

Entropy Coding
~~~~~~~~~~~~~~

After quantization, **Huffman coding** (a prefix-free code) encodes symbols based on their frequency. The theoretical lower bound is the **entropy**:

.. math::

   H = -\sum P(s) \log_2 P(s)

where :math:`P(s)` is the probability of symbol :math:`s`.

Resources
~~~~~~~~~

* http://www.ImageProcessingPlace.com
