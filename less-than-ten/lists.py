numberRange = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newRange = []
secondRange = []
userInput = input("Enter a number to create a list for all numbers less than your number or equal to. \n")
userInput = float(userInput)
for x in numberRange:
    if x <= 5 and x not in newRange:
        newRange.append(x);

print(newRange);

for num in numberRange:
    if num <= userInput and num not in secondRange:
        secondRange.append(num)
print (secondRange)

