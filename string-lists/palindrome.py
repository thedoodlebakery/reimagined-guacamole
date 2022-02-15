# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

userString = input("Please type in a palindrome. (Palindrome is a word that reads the same way forwards and backwards.) \n")

# reverse string
# check

# declare backwardsString
backwardsString = userString[::-1]

# newString.append(userString) - will not work for a string
# [:: -1]takes a string makes a slices of each letter from the end of the word moving ?# left then puts the string in reverse order. Its like a list[start:end:step]

if backwardsString == userString:
    print("Yes this is palindrome")
else:
    print("This is word is not a palindrome.")

print(userString)
print (backwardsString)



