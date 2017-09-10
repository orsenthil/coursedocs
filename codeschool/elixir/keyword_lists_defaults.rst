Keyword Lists and Defaults
==========================

::

    Account.balance(transactions)


Passing options with keyword lists
----------------------------------


::

    Account.balance(..., currency: "dollar", symbol: "$:)


And this is same as

::

    Account.balance(..., [{:currency, "dollar"}, {:symbol, "$"}])



Reading Keyword Lists
---------------------

::

    defmodule Account do

        def balance(transactions, options) do
            currency = options[:currency]
            symbol = options[:symbol]

            balance = calculate_balance(transactions)
            "Balance in #{currency}: #{symbol}#{balance}"
        end
        ...
    end

::


    Account.balance(transactions, currency: "dollar", symbol: "$")

Must Pass All Arguments
-----------------------

::

    defmodule Account do
        def balance(transactions, options \\ []) do
            currency = options[:currency]
            symbol = options[:symbol]
            ...
        end
        ...
    end

With default values

::

    Account.balance(transactions)

     defmodule Account do
        def balance(transactions, options \\ []) do
            currency = options[:currency] || "dollar"
            symbol = options[:symbol] || "$"
            ...
        end
        ...
    end

    Account.balance(transactions)


Example of Library in Elixer

* https://github.com/elixir-ecto/ecto

::

    Repo.all(from u in User, where: u.age > 21, where: u.is_active == true)
