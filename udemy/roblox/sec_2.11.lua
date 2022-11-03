local myPart = script.Parent

-- debounce

local db = true

local function partTouchedFunction(partTouched)
    if db then
        db = false
        myPart.BrickColor = BrickColor.Random()
        wait(2)
        db = true
    end
end

myPart.Touched:Connect(partTouchedFunction)
