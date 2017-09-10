2A-L6 Edge detection: 2D Operators
==================================


::

    % For Your Eyes Only
    pkg load image;

    frizzy = imread('frizzy.png');
    froomer = imread('froomer.png');
    imshow(frizzy);
    imshow(froomer);

    % Find edge in frizzy and froomer images
    frizzy_gray = rgb2gray(frizzy);
    froomer_gray = rgb2gray(froomer);

    frizzy_edges = edge(frizzy_gray, 'canny');
    froomer_edges = edge(froomer_gray, 'canny');
    imshow(frizzy_edges);
    imshow(froomer_edges);

    % TODO: display common edge pixels

    imshow(frizzy_edges & fromer_edges);

