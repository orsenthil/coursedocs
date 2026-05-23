local age = 15
local movieRating = "M"

if age >= 15 then
    print("You can watch the M rated movie")
else
    print("You are too young to watch the M rated movie")
end

movieRating = "G"

if movieRating == "G" then
    print("You can watch the G rated movie")
end

movieRating = "M"

if age >= 15 and movieRating == "M" then
    print("You can watch the M rated movie")
end

