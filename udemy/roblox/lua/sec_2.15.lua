-- Create a Spawn point.
-- Create a part to pick up. Rename it to "Pickup"
-- Anchored
-- Add a Script and rename it to pickupScript
--
local sign = game.Workspace.signModel.backboard.SurfaceGui.Frame.TextLabel
local pickup = script.Parent
local db = true

pickup.Touched:Connect(function(hit)
    local character = hit.Parent
    local humanoid = character:FindFirstChild("Humanoid")
    if humanoid and db then
        local player = game.Players:GetPlayerFromCharacter(character)
        -- game.Players:FindFirstChild(character.Name)

        db = false

        pickup.Transparency = 1
        pickup.CanCollide = false

        sign.Text = "You have picked up the item!"

        print(player.Name .. " picked up the part!")

        wait(5)

        pickup.Transparency = 0
        pickup.CanCollide = true

        sign.Text = "Pick up the part!"

        db = true
    end

end)

