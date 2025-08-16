Python
======


* `C Programming <https://www.cprogramming.com>`_
* `PyAlgo Viz <https://pyalgoviz.appspot.com/>`_
* `Doing HTTP Request Inline <https://prestigemad.com/#!/doc/browser/master>`_
* `Curl Converter <https://curlconverter.com/>`_
* The official `Python Developer’s Guide <https://devguide.python.org/>`_
* `Your Guide to the CPython Source Code <https://realpython.com/cpython-source-code-guide/>`_ (Aug 2019) by Anthony Shaw
* `Internals of CPython 2.7 <https://intopythoncom.files.wordpress.com/2017/04/internalsofcpython2-7.pdf>`_
* `Internals of CPython 3.6 <https://intopythoncom.files.wordpress.com/2017/04/internalsofcpython3-6-1.pdf>`_
* `Advanced Internals of CPython 3.6 <https://intopythoncom.files.wordpress.com/2017/04/merged.pdf>`_
* `Python Development Documentation <https://pythondev.readthedocs.io/>`_ by Victor Stinner
* `CPython internals: A ten-hour codewalk through the Python interpreter source code <http://pgbovine.net/cpython-internals.htm>`_ (October 2014) by Philip Guo
* `Lifecycle of a Python Code - CPython's Execution Model <https://web.archive.org/web/20190427101546/https://dev.to/btaskaya/lifecycle-of-a-python-code---cpythons-execution-model-85i>`_ by Batuhan Osman Taşkaya (October 2018)
* `A Python Interpreter Written in Python <http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html>`_ (2016) by Allison Kaptur, from `500 Lines or Less <http://aosabook.org/en/index.html>`_ book.
* https://blog.sourcerer.io/python-internals-an-introduction-d14f9f70e583

.. code-block:: bash

   brew install pkg-config openssl xz gdbm tcl-tk

Clone
-----

.. code-block:: bash

   gh repo clone python/cpython

Version of Brew Installed Package
---------------------------------

.. code-block:: bash

   brew info openssl

Python 3.10
-----------

.. code-block:: bash

    PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig" \
      ./configure --with-pydebug --with-openssl=$(brew --prefix openssl@3)

With Address Sanitizer for Debugging
------------------------------------

.. code-block:: bash

    set -e
    set -u
    set -o pipefail
    set -x

    dir="builds/simple"
    here="$(realpath .)"

    mkdir --parent "${dir}"
    pushd "${dir}"

    export CC="clang"
    export LD="clang"
    export ASAN_OPTIONS=detect_leaks=0
    export MSAN_OPTIONS=poison_in_dtor=0
    export CFLAGS="-fno-sanitize-recover"
    nice "${here}/configure" \
    --with-assertions \
    --with-pydebug \
    --disable-ipv6 \
    --with-trace-refs \
    --with-undefined-behavior-sanitizer \
    --with-address-sanitizer \

    # --with-memory-sanitizer \

    nice make -j8
    nice make test


    export CFLAGS="-fno-sanitize-recover -fwrapv"

Python 3.12
-----------

.. code-block:: bash

    export PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"

    ./configure --with-pydebug \
                  --with-openssl=$(brew --prefix openssl@3) \
                  --with-tcltk-libs="$(pkg-config --libs tcl tk)" \
                  --with-tcltk-includes="$(pkg-config --cflags tcl tk)"

C Programming
-------------

* Let us C - https://archive.org/details/let-us-c/page/251/mode/2up


Setup Python with custom OpenSSL
--------------------------------


::

    cd ~
    wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz
    wget https://www.openssl.org/source/openssl-1.1.1b.tar.gz.sha256
    sha256sum openssl-1.1.1b.tar.gz
    cat openssl-1.1.1b.tar.gz.sha256
    tar zxvf openssl-1.1.1b.tar.gz
    ls /home/senthilx/
    cd openssl-1.1.1b
    ./config \
        --prefix=/home/senthilx/custom-openssl \
        --libdir=lib \
        --openssldir=/etc/ssl
    make -j1 depend
    make -j8
    make install_sw

    cd ~
    cd cpython
    ./configure -C --with-openssl=/home/senthilx/openssl --with-openssl-rpath=auto --prefix=/home/senthilx/python-3.x.x
    make
    make install

CPython Internals
-----------------



