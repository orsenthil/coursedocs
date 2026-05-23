local allSteps = workspace.magicStepsModel.stepModel:GetChildren()

while wait(1) do
    local randNum = math.random(1, #allSteps)
    local randStep = allSteps[randNum]

    for i=0, 1, .2 do
        task.wait(.1)
        randStep.Transparency = i
    end

    randStep.CanCollide = false

    wait(.5)

    for i=1, 0, -0.2 do
        wait(.1)
        randStep.Transparency = i
    end

    randStep.CanCollide = true
end
