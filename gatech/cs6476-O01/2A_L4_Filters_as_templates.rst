2A-L4 Filters as templates
==========================


Find Template 1D Quiz
---------------------

::

    % Find template 1D

    pkg load image;

    function index = find_template_1D(t, s)
        c = normxcorr2(t, s);
        [maxValue rawIndex] = max(c);
        index = rawIndex - size(t, 2) + 1;
    endfunction

    s = [-1 0 0 1 1 1 0 -1 -1 0 1 0 0 -1];
    t = [1 1 0];

    disp('Signal:'), disp([1: size(s, 2); s]);
    disp('Template:'), disp([1: size(t, 2); t]);

    index = find_template_1D(t, s);
    disp('Index:'). disp(index);


Template Matching
-----------------


