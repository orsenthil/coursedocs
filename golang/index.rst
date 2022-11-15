Go Programming Language
=======================

Go Language
-----------

::

    GOROOT="/usr/local/go"
    GOPATH="/Users/senthilx/go"

    GOPRIVATE=""
    GOPROXY="direct"

Go code organization

I set this up in bash profile.

::

    export GOROOT="/usr/local/go"
    export GOPATH="/home/senthilx/go"

    export GOPRIVATE=""
    export GOPROXY="direct"

::

    go install golang.org/x/tools/cmd/goimports@latest

Installed `vim-go <https://github.com/fatih/vim-go>`_ as the only plugin to work with the default vim.
Made sure my ide is working without red lines.

https://vimawesome.com/

How to use slices in go?

::

     var slice := []int
     slice = append(slice, 10)

Go Proxy
--------

::

    go env -w GOPROXY=direct

Install the latest version
--------------------------

::

   go install golang.org/dl/go1.19.1@latest
   go1.19.1 download
   echo "export PATH=~/sdk/go1.19.1/bin:$PATH" >> ~/.bashrc
   source ~/.bashrc
   go version



How to test go code
-------------------

1. Write it in play.golang.org
2. Use this template

.. code-block::

    package main

    import (
        "log"
        "time"
    )

    func main() {
        date := "7/25/2019 13:45:00" # "7/25/2019 13:45:00"
        timeT, err := time.Parse("1/2/2006 15:04:05", date)

        if err != nil {
            log.Fatalf("Error parsing: %v", err)
        }

        log.Printf("Got: %v", timeT)
    }

3. Modify and Test
4. Advantages sharable, and no need to create cruft.

Example play link - https://play.golang.org/p/73Gt3O1Ok-1
