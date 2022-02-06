number = input("Type in a number.\n");
number = int(number);
num1 = input("Type a random number.\n");
check = input("Type a second number.\n");

if number % 2 == 0:
    print(str(number) + " is even.");
    if number % 4 == 0:
        print(str(number) + " is a multiple of 4.")
else:
    print(str(number) + " is odd.")

if (float(num1))%(float(check)) == 0:
    print(num1 + " is divisible by " + check);
else: 
    print(num1 + " is not divisible by " + check);