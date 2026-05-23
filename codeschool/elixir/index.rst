Elixir
======

Notes from the CodeSchool Elixir course.


Tuples
------

A **tuple** is a fixed-size collection — written with curly braces:

.. code-block:: elixir

    {}
    {:ok, "some content"}
    {:error, "some error occurred"}

Pattern matching on tuples:

.. code-block:: elixir

    {status, content} = {:ok, "some content"}
    {:error, message} = {:error, "some error occurred"}

**Returning tuples from functions** — a common Elixir convention for success/failure:

.. code-block:: elixir

    {:ok, content} = File.read("transactions.csv")
    # {:error, reason} when the file does not exist

.. code-block:: elixir

    defmodule Account do
      def parse_file({:ok, content}) do
        IO.puts "Transactions: #{content}"
      end

      def parse_file({:error, _error}) do
        IO.puts "Error parsing file"
      end
    end


Lists and Recursion
-------------------

Reading elements from a list using the **cons** operator (``|``):

.. code-block:: elixir

    languages = ["Elixir", "JavaScript", "Ruby"]
    [head | tail] = languages

Pattern matching in function heads:

.. code-block:: elixir

    defmodule Language do
      def print_list([head | tail]) do
        IO.puts "Head: #{head}"
        IO.puts "Tail: #{inspect(tail)}"
      end
    end

**Recursion** — two cases:

- **Base case** (terminating): function does not call itself (e.g. empty list ``[]``).
- **Recursive case**: computation happens, then the function calls itself.

.. code-block:: elixir

    defmodule Language do
      def print_list([head | tail]) do
        IO.puts head
        print_list(tail)
      end

      def print_list([]) do
      end
    end


Control Flow
------------

The ``case`` Statement
~~~~~~~~~~~~~~~~~~~~~~

Replace nested ``if`` with ``case`` for cleaner branching:

.. code-block:: elixir

    defmodule Account do
      def list_transactions(filename) do
        {result, content} = File.read(filename)
        case result do
          :ok -> "Content: #{content}"
          :error -> "Error: #{content}"
        end
      end
    end

Pattern match directly on the tuple returned by ``File.read/1``:

.. code-block:: elixir

    defmodule Account do
      def list_transactions(filename) do
        case File.read(filename) do
          {:ok, content} -> "Content: #{content}"
          {:error, type} -> "Error: #{type}"
        end
      end
    end

**Guard clauses** — add conditions to pattern matches:

.. code-block:: elixir

    defmodule Account do
      def list_transactions(filename) do
        case File.read(filename) do
          {:ok, content} when byte_size(content) > 10 -> "Content: (...)"
          {:ok, content} -> "Content: #{content}"
          {:error, type} -> "Error: #{type}"
        end
      end
    end


The ``cond`` Statement
~~~~~~~~~~~~~~~~~~~~~~

Use ``cond`` when you need multiple conditional branches (like a multi-branch ``if/else``):

.. code-block:: elixir

    Account.transfer_amount(123535353, 252224, 150.40)  # -> {:ok, "Success"}
                                                        # -> {:error, "Failure"}

Transfer validation depends on amount and hour of day:

.. code-block:: elixir

    defmodule Account do
      def transfer_amount(from_account, to_account, amount) do
        hour_of_day = DateTime.utc_now().hour

        if valid_transfer?(amount, hour_of_day) do
          perform_transfer(from_account, to_account, amount)
        else
          {:error, "Invalid Transfer"}
        end
      end
    end

.. code-block:: elixir

    def valid_transfer?(amount, hour_of_day) do
      cond do
        hour_of_day < 12 -> amount <= 5000
        hour_of_day < 18 -> amount <= 1000
        true -> amount <= 300
      end
    end


Maps
----

Maps are key-value stores (similar to hashes/dictionaries):

.. code-block:: elixir

    person = %{"name" => "Brooke", "age" => 42}

**Reading with ``Map.fetch/2`` and ``Map.fetch!/2``**

.. code-block:: elixir

    Map.fetch(person, "name")    # {:ok, "Brooke"}
    Map.fetch(person, "banana")  # :error
    Map.fetch!(person, "name")   # "Brooke" (raises KeyError if missing)

**Pattern matching on maps**

.. code-block:: elixir

    person = %{"name" => "Brooke", "age" => 42}
    %{"name" => name, "age" => age} = person

Match only the keys you need:

.. code-block:: elixir

    %{"name" => name} = person

Nested maps:

.. code-block:: elixir

    person = %{
      "name" => "Brooke",
      "address" => %{"city" => "Orlando", "state" => "FL"}
    }

    %{"address" => %{"state" => state}} = person
    IO.puts "State: #{state}"


Keyword Lists and Defaults
--------------------------

Keyword lists pass options as ``key: value`` pairs:

.. code-block:: elixir

    Account.balance(transactions, currency: "dollar", symbol: "$")

Equivalent to a list of tuples:

.. code-block:: elixir

    Account.balance(transactions, [{:currency, "dollar"}, {:symbol, "$"}])

Reading keyword list options:

.. code-block:: elixir

    defmodule Account do
      def balance(transactions, options) do
        currency = options[:currency]
        symbol = options[:symbol]
        balance = calculate_balance(transactions)
        "Balance in #{currency}: #{symbol}#{balance}"
      end
    end

**Default arguments** — make ``options`` optional with ``\\ []``:

.. code-block:: elixir

    defmodule Account do
      def balance(transactions, options \\ []) do
        currency = options[:currency] || "dollar"
        symbol = options[:symbol] || "$"
        # ...
      end
    end

    Account.balance(transactions)  # uses defaults

Example from the Ecto library:

.. code-block:: elixir

    Repo.all(from u in User, where: u.age > 21, where: u.is_active == true)


Anonymous Functions
-------------------

Named function:

.. code-block:: elixir

    defmodule Account do
      def max_balance(amount), do: "Max: #{amount}"
    end

Anonymous function syntax (``fn``):

.. code-block:: elixir

    max_balance = fn amount -> "Max: #{amount}" end
    max_balance.(500)

Pass functions as arguments:

.. code-block:: elixir

    deposit = fn balance, amount -> balance + amount end
    withdrawal = fn balance, amount -> balance - amount end

    Account.run_transaction(1000, 20, deposit)     # -> 1020
    Account.run_transaction(1000, 20, withdrawal)  # -> 980
    Account.run_transaction(0, 20, deposit)        # -> "Cannot perform any transaction"

.. code-block:: elixir

    defmodule Account do
      def run_transaction(balance, amount, transaction) do
        if balance <= 0 do
          "Cannot perform any transaction"
        else
          transaction.(balance, amount)
        end
      end
    end

**Pattern matching in anonymous functions** (multiple clauses):

.. code-block:: elixir

    account_transaction = fn
      balance, amount, :deposit -> balance + amount
      balance, amount, :withdrawal -> balance - amount
    end

**Capture operator shorthand** (``&``):

.. code-block:: elixir

    deposit = &(&1 + &2)
    Account.run_transaction(1000, 20, deposit)
    Account.run_transaction(1000, 20, &(&1 + &2))
    Enum.map([1, 2, 3, 4], &(&1 * 2))


Mix Projects
------------

**Mix** is Elixir's build tool — manages project structure, compilation, dependencies, and collaboration.

Create a new project:

.. code-block:: shell

    mix new budget

Run code in the project context:

.. code-block:: shell

    mix run -e "Budget.current_balance(100, 20) |> IO.puts"

``mix run`` does three things:

1. Compiles the application.
2. Loads bytecode into the Erlang VM.
3. With ``-e``, evaluates the given expression.

**Third-party dependencies** — declare in ``mix.exs``:

.. code-block:: elixir

    defmodule Budget.Mixfile do
      defp deps do
        [{:httpoison, "~> 0.10.0"}, {:poison, "~> 3.0"}]
      end
    end

.. code-block:: shell

    mix deps.get

**HTTP calls with HTTPoison** (example conversion module):

.. code-block:: elixir

    defmodule Budget.Conversion do
      def from_euro_to_dollar(amount) do
        url = "https://cs-currency-rates.herokuapp.com/currency-rates"
        case HTTPoison.get(url) do
          {:ok, response} -> parse(response) |> convert(amount)
          {:error, _} -> "Error fetching rates"
        end
      end

      defp parse(%{status_code: 200, body: json_response}) do
        Poison.Parser.parse(json_response)
      end

      defp convert({:ok, rates}, amount) do
        rate = find_euro(rates)
        amount * rate
      end

      defp find_euro([%{"currency" => "euro", "rate" => rate} | _]), do: rate
      defp find_euro([_ | tail]), do: find_euro(tail)
      defp find_euro([]), do: raise "No rate found for Euro"
    end

.. code-block:: shell

    mix run -e "Budget.Conversion.from_euro_to_dollar(15) |> IO.puts"
