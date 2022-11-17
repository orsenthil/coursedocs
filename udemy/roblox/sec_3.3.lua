-- logScript

local log = script.Parent
local db = true

log.Touched:Connect(function(hit)
    local character = hit.Parent
    local hum = char:FindFirstChild("Humanoid")

    if db and hum then
        db = false

        local plr = game.Players:FindFirstChild(char.Name)
        local pStats = plr:WaitForChild("leaderstats")

        log.Transparency = 1
        wait(3)
        log.Transparency = 0

        db = true
    end

end)
