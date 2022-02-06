
# # Exercise 5: Write a Python program to create a dictionary that stores your first name, last name and year of your birthday. 
# # Finally, print each data into a message. (You can create a function, but it is optional)

# ### Type code here
# thisdict =	{
#   "first name": "Christina",
#   "last name": "Bolden",
#   "year": 1990
# }
# #print(thisdict)
# print("My name is " + thisdict['first name'] + " " + thisdict['last name'] + " " + "and my birthday is in " + str(thisdict['year']))



# # thisdict =	{
# #   "first name": "Christina",
# #   "last name": "Bolden",
# #   "year": 1990
# # }
# for x in thisdict:
#     print("My name is Christina Bolden and my birthday is in 1990")


# number = 3

# if type(number) == int or type(number) == float:
#   if number%2 == 0: 
#     print("This is even.")
#     #print(number%2)
#   else:
#     #print(number%2)    
#     print("This is odd.")
# else:
#   print("This is not a number.")


#a = 2
#b = 9
#c = 8

#if c/a:
#  print("c is even")
#elif a==c:
# print("a is equal to c")
#else:
#  print("b is not divisible by 2")   
  

# ====================================

# Exercise 4: Write a Python program to print True if the number in the list is even or False if it is odd using a for loop. (You can create a function, but it is optional)

# step 1: create a loop to iterate from the beginning to the end of the list
# Hint: remember lists in python start by 0
# step 2: do a conditional to check if "number" is divisible by 2 (even) or not (odd).
# Hint: you need to check if an integer is divisible by other, and to do that you need to check if the remainder of division is zero
# step 3: print "True" or "False" according to the conditional statement (if it is true or false)

  #list of integers
list = [1, 2, 7, 10, 15, 20, 50]

#asigning divisible numbers
# a = 2
# b = 3

#print this list
# print ("List is:  ", list)

#checking if these numbers are divisible by a or b
#or not, if condition is true print to the element
# txt = "Numbers divisble by {2} and {3}"
# print(txt.format(a,b) 

#list of integers
list = [1, 2, 7, 10, 15, 20, 50]

for num in list:
  if(num % 2 == 0): 
    #print this list   
    print ("True, " + str(num) + " is divisible by 2.")
  else: 
    #print this list
    print("False, " + str(num) + " is not divisible by 2.")