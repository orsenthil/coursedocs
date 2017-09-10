2A L5 Edge detection: Gradients
===============================


Gradient Direction Quiz
-----------------------

::

    % Gradient Direction
    pkg load image;

    function result = select_gdir(gmag, gdir, mag_min, angle_low, angle_high)
        result = gmag >= mag_min & angle_low <= gdir & gdir <= angle_high;
    endfunction

    % Load and convert image to double type, range [0, 1] for convenience
    img = double(imread('octagon.png')) / 255
    imshow(img);    % assumes [0, 1] range for double images

    % Compute x, y gradients
    [gx gy] = imgradientxy(img, 'sobel');
    imshow((gy + 4) / 8);   % or imshow(gx, [-4 4]) or imshow(gy, []) or imagesc()

    % Obtain gradient magnitude and direction
    [gmag gdir] = imgradient(gx, gy);
    imshow(gmag / (4 * sqrt(2))); % gmag = sqrt(gx^2 + gy^2), so: [0, (4 * sqrt(2))]
    % imshow((gdir + 180.0) / 360.0);

    % Find pixels with desired gradient direction
    my_grad = select_gdir(gmag, gdir, 1, 30, 60); % 45 +/- 15
    imshow(my_grad);

