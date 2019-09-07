The cond statement
==================

.. code-block:: guess


    Account.transfer_amount(123535353, 252224, 150.40) -> {:ok, "Success"}
                                                    -> {:error, "Failure"}

Transfer Depends on Validation
------------------------------

The validation for a transfer involves the amount transferred and the hour of the day.

.. code-block:: guess

    defmodule Account do
        def transfer_amount(from_amount, to_account, amount) do
            hourOfDay = DateTime.utc_now.hour

            if ! valid_transfer?(amount, hourOfDay) do
                {:error, "Invalid Transfer"}
            else
                perform_transfer(from_account, to_account, amount)
            end

        end
    end

The cond statement
------------------

.. code-block:: guess


    def valid_transfer?(amount, hourOfDay) do
        cond do
            hourOfDay < 12 -> amount <= 5000
            hourOfDay <18 -> amount <= 1000
            true -> amount <= 300
        end
    end


.. image:: https://dl.dropbox.com/s/sczz7kuqssjn4z5/Screenshot%202017-09-09%2006.49.54.png?dl=0
   :width: 640
   :height: 580
