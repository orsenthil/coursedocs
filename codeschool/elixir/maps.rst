Maps
====

::

    person = %{ "name" => "Brooke", "age" => 42}


Reading Maps With Map.fetch and Map.fetch!
------------------------------------------

The Map module from Elixer's standard offers a set of functions for working with maps.

::

    {:ok, "Brooke"} Map.fetch(person, "name")


* It returns a tuple when key is present.

And the :error atom when it is not.

::

    :Map.fetch(person, "banana") // returns :error atom

    Map.fetch!(person, "name") // returns the person name if present.

    and raises an Keyerror exception if the person is not present.


Reading Maps with pattern Matching
----------------------------------

::

    person = %{"name" => "Brooke", "age" => 42}
    %{ "name" => name, "age" => age } = person
    IO.puts name


We can pattern match only the portion that we are interested in.

::

    person = %{"name" => "Brooke", "age" => 42}
    %{"name" => name} = person
    IO.puts name


    person = %{ "name" => "Brooke",
                "address" => %{ "city" => "Orlando",
                                "state" => "FL" }}


    %{ "address" => %{ "state" => state }} = person

    IO.puts "State: #{state}"

