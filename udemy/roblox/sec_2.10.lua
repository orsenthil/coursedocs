local myPart = script.Parent

myPart.BrickColor = BrickColor.Random()

local function partTouchedFunction(partTouched)
    print(partTouched)
end

myPart.Touched:Connect(partTouchedFunction)
