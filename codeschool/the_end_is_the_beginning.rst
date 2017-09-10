Reading Elements From a List

::

    languages = ["Elixer", "JavaScript", "Ruby"]

    [head | tail] = languages


Using cons in Function Pattern Matching

::

    defmodule Language do
        def print_list([head | tail]) do
            IO.puts "Head: #{head}"
            IO.puts "Tail: #{tail}"
        end
    end


Understanding Recursion
-----------------------

::

    defmodule Language do
        def print_list([head | tail]) do
            IO.puts head
            print_list(tail)
        end

        def print_list([]) do
        end
    end


.. image:: https://dl.dropbox.com/s/pdxjrzjox72qc43/Screenshot%202017-09-03%2021.25.12.png?dl=0
   :align: center
   :height: 300
   :width: 450

Two Cases for Recursion

* The base case, also called terminating scenario, where the function does NOT invoke itself.
* The recursive case, where computation happens and the function invokes itself.

