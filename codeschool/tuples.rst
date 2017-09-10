Tuples
======


::

    {}


A valid tuple.

::

    {:function, "elixer", 2012}

    {status, content} = {:ok, "some content"}

    {:error, message} = {:error, "some error occurred."}


Returning Tuples From Functions

::

    {status, content} = File.read()

    {:ok, content} = File.read("transactions.csv")
    {:ok, content} = File.read("file-that-doesnt-exist")


::

    defmodule Account do
        def parse_file({:ok, content}) do
            IO.puts "Transactions: #{content}"
        end

        def parse_file({:error, error}) do
            IO.puts "Error parsing file"
        end
    end
