local myPart = script.Parent

-- debounce

local db = true

myPart.Touched:Connect(function(partTouched)
    if db then
        db = false
        myPart.BrickColor = BrickColor.Random()
        wait(2)
        db = true
    end
end)
