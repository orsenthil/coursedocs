-- mainScript
game.Players.PlayerAdded:Connect(function(player)
    player.CharacterAdded:Connect(function(character)

        local leaderstats = Instance.new("Folder")
        leaderstats.Name = "leaderstats"
        leaderstats.Parent = player

       end)
end)
