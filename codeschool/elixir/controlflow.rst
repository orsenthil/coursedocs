Control Flow
------------

The case statement
------------------

.. code-block:: guess

    defmodule Account do
        def list_transactions(filename) do
            {result, content} = File.read(filename)

            if result == :ok do
                "Content: #{content}"
            else
                if result == :error do
                    "Error: #{content}"
                end
            end
        end
    end


.. code-block:: guess

    defmodule Account do
        def list_transactions(filename) do
            {result, content} = File.read(filename)
            case result do
                :ok -> "Content: #{content}"
                :error -> "Error: #{content}"
            end
        end
    end

The pattern matching can be over tuples.

.. code-block:: guess

    defmodule Account do
        def list_transactions(filename) do
            case File.read(filename) do
                {:ok, content} -> "Content: #{content}"
                {:error, type } -> "Error: #{type}"
            end
        end
    end

Using case with Guard Clauses
-----------------------------

.. code-block:: guess

    defmodule Account do
        def list_transactions(filename) do
            case File.read(filename) do
            {:ok, content}
                when byte_size(content) > 10 -> "Content: (...)"
            {:ok, content} -> "Content: #{content}"
            {:error, type} -> "Error: #{type}"
        end
    end