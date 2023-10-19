-- Add this 1
local wall = workspace.iceWall

local myName = "Bill"
local myAge = 12
local isAllowedToGoCamping = true

-- Add this 3
task.wait(5)

-- Add this 2
if myName == "Bill" then
    print("Yes your name is ", myName)
    wall.Transparency = 0.3
else
    warn("No your name is not Bill")
end

task.wait(5)

if myAge >= 10 then
    print("Yes you are ", myAge, " you are old enough to go camping")
    wall.Transparency = 0.6
end

if isAllowedToGoCamping == true then
    print("Yes you are allowed to go camping")
    wall.Transparency = 1
    wall.CanCollide = false
end
