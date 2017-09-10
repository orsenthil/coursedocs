Anonymous Functions
-------------------

::

    defmodule Account do
        def max_balance(amount) do
            "Max: #{amount}"
        end
    end


We will use this syntax.

::

    fn -> syntax


::

    max_balance = fn(amount) -> "Max: #{amount}" end


::

    max_balance.(500)


::

    Account.run_transaction(100, 20, deposit)
    Account.run_transaction(100, 20, withdrawal)


::

    defmodule Account do
        def run_transaction(balanace, amount, transaction) do
            if balance <= 0 do
                "Cannot perform any transaction"
            else
                transaction.(balance, amount)
            end
        end
    end

::

    deposit = fn(balance, amount) -> balance + amount end
    withdrawal = fn(balance, amount) -> balance - amount end


    Account.run_transaction(1000, 20, withdrawal) -> 980
    Account.run_transaction(1000, 20, deposit) - 1020
    Account.run_transaction(0, 20, deposit)  -> "Cannot perform any transaction"


Pattern Matching in Anonymous Functions


::

    account_transaction = fn
        (balance, amount, :deposit) -> balance + amount
        (balance, amount, :withdrawal) -> balance - amount
    end

Anonymous Function Shorthand Syntax

::

    deposit = fn(balance, amount) -> balance + amount end

    deposit = &(&1 + &2)

    Account.run_transaction(1000, 20, deposit)

    Account.run_transaction(1000, 20, &(&1 + &2))

    Enum.map([1, 2, 3, 4], &(&1 * 2))

