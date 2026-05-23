local myNum = 0
local myBool = true

while myBool == true do
    myNum = myNum + 1
    print(myNum)
    if myNum == 10 then
        myBool = false
    end
end

print("The while loop has ended", myBool)
print("The final value of myNum is", myNum)