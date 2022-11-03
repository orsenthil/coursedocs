-- Player = This is you!
-- Humanoid - A little robot
-- Character - This is how you look in the game.
--

local myPart = script.Parent

-- debounce

local db = true

myPart.Touched:Connect(function(hit)
    local character = hit.Parent
    local humanoid = character:FindFirstChild("Humanoid")
    if humanoid and db then
        local player = game.Players:GetPlayerFromCharacter(character)
        -- game.Players:FindFirstChild(character.Name)
        db = false
        myPart.BrickColor = BrickColor.Random()
        print(player.Name .. " touched the part!")
        wait(2)
        db = true
    end

end)


-- Test this. Player can change the color of the part by touching it.
-- Moving another block against it will not change the color.
