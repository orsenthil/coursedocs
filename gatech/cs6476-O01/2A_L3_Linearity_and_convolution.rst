Linearity and Convolution
=========================

Methods
-------


.. image:: https://dl.dropbox.com/s/vfaerx8i0jb40py/Screenshot%202017-09-10%2006.55.27.png?dl=0
   :align: center
   :height: 300
   :width: 450


.. image:: https://dl.dropbox.com/s/9hqxm71x6y0ljcd/Screenshot%202017-09-10%2006.56.11.png?dl=0
   :align: center
   :height: 300
   :width: 450

::

    % Explore edge options
    pkg load image;

    %% Load an image
    img = imread('fall-leaves.png');  % also available: peppers.png, mandrill.png
    imshow(img);

    %% TODO: Create a Gaussian filter
    filter_size = 21;
    filter_sigma = 3;
    filter = fspecial('gaussian', filter_size, filter_sigma);

    %% TODO: Apply it, specifying an edge parameter (try different parameters)

    smoothed = imfilter(img, filter, 0);

    %% smoothed = imfilter(img, filter, 'circular')
    %% smoothed = imfilter(img, filter, 'replicate')
    %% smoothed = imfilter(img, filter, 'symmetric')


Apply A Median Filter
---------------------

::

   % Apply a Median filter

   pkg load image;

   %% Read an image
   img = imread('moon.png');
   imshow(img)

   %% Add salt and pepper noise
   noisy_img = imnoise(img, 'salt & pepper', 0.02);
   imshow(noisy_img)

   %% Apply a median filter
   median_filtered = medfilt2(noisy_img)
   imshow(median_filtered)

