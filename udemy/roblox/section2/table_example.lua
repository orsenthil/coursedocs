-- An empty table

local myTable = {}

-- Add an item to the table

myTable[1] = "banana"

table.insert(myTable, "orange")

print(table)

for i=1, #myTable do
    print(myTable[i])
end

local boxTable = workspace.boxModel:GetChildren()

print(boxTable)

boxTable[4].BrickColor = BrickColor.new("Really red")

