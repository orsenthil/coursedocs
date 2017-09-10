Color Planes
------------


::

    img = imread('fruit.png')
    imshow(img);

    disp(size(img));


Selecting the red channel

::

    img_red = img(:, :, 1);
    imshow(img_red);

    disp(img_red)
    plot(img_red(150, 0))


::

    img = imread('fruit.png');
    imshow(img);

    disp(size(img));

To plot a row of pixels, the statement should be.

::

    plot(img_red(150, :));


Add 2 Images Demo
-----------------


::

    % Add two images
    dolphin = imread('dolphin.png')
    bicycle = imread('bicycle.png')

    imshow(dolphin);
    disp("Dolphin image size:");
    disp(size(dolphin));

    imshow(dolphin);
    disp("Bicycle image size:");
    disp(size(bicycle));

    summed = dolphin + bicycle;

    average_alt = (dolphin / 2) + (bicycle / 2);
    imshow(average_alt)

Multiplying By Scalar Demo
--------------------------

::

    function result = scale(img, value)
        result = value .* img;
    endfunction


Quiz: Blend 2 Images
--------------------

% Blend two images

::

    dolphin = imread("dolphin.png")
    bicycle = imread("bicycle.png")

    result = 0.75 * dolphin + 0.25 * bicycle;
    imshow(result)

Blending two images.

::

    function output = blend(a, b, alpha)
        % TODO: Your code here; finally assign: output = <something>;
        output = alpha * a + b;
    endfunction

Noise in images
---------------

Noise is just another function that is combined with the original function to get a new function.

::

    I(x, y) = I(x, y) + n(x, y)


* Salt and Pepper Noise.
* Impulse Noise
* Gaussian Noise

Gaussian Noise
--------------

::

    noise = randn(size(im)) .* sigma;
    output = im + noise;


Image Difference Demo
---------------------

::

    dolphin = imread('dolphin.png');
    bicycle = imread('bicycle.png');

    diff = dolphin - bicycle;

    imshow(diff)

    abs_diff = abs(bicycle - dolphin);
    imshow(abs_diff)


We are losing out negative values in the result.

::

    % Better: Use image package
    pkg load image;

    abs_diff2 = imabsdiff(dolphin, bicycle);    // order doesn't matter.
    imshow(abs_diff2);


Generate Gaussian Noise
-----------------------

::

    some_number = randn();
    disp(some_number);

    some_numbers = randn([1 5]);
    disp(some_numbers);


::

    noise = randn([1 100])
    [n, x] = hist(noise, [-3 -2 -1 0 1 2 3]);
    disp([x; n]);
    plot(x, n);


Generate gaussian noise with linspace
-------------------------------------

::

    noise = randn([1 100]);
    [n, x] = hist(noise, linspace(-3, 3, 7));
    %disp([x; n]);
    plot(x, n);

    noise = randn([1 1000]);
    [n, x] = hist(noise, linspace(-3, 3, 21));
    %disp([x; n]);
    plot(x, n);

    noise = randn([1 10000]);
    [n, x] = hist(noise, linspace(-3, 3, 21));
    plot(x, n);

    noise = randi([1 100000]);
    [n, x] = hist(noise, linspace(-3, 3, 21));
    plot(x, n);


Trying simple things
--------------------

::

    % TODO: Try generating other kinds of random numbers.
    %       How about a 2D grid of random Gaussian values?

    noise = randn([1 10, 1 10])

    [n x] = hist(noise, linspace(-3, 3, 21));

    plot(x, n)


Effect of Sigma of Gaussian Noise
---------------------------------

Showing you images of Gaussian noise.

::

    noise = randn(size(im)).* sigma;


    Images shows the noise values themselves. Grey is zero.


Apply Gaussian Noise Quiz
-------------------------

::

    noise = randn(size(img)) .* 2;

    img = imread("saturn.png")
    imshow(img)

    noise = randn(size(img)) .* 100;
    output = img + noise;
    imshow(output);


Displaying Images in Matlab
---------------------------

::

    imshow(im, [LOW, HIGH])
    imshow(im, [])

