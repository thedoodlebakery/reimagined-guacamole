from datetime import date

userName = input("What is your name?");

userAge = input("How old are you?");

todaysDate = date.today();

random_number = int(input("Give us a random number."));


def centuryOld():
    years_to_hundred = (100 - (int(userAge))-1);
    century_year = str(years_to_hundred + todaysDate.year);
    print("Hi " + userName + ", you will turn one hundred in " + century_year + " \n");

centuryOld();


