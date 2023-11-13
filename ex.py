import datetime

year_of_birth = int(input("enter year: "))

current_year = datetime.datetime.now().year

if year_of_birth < 1900 or year_of_birth > current_year:
    print("Error: The birth year entered is not valid")
else:
    age = current_year - year_of_birth

    if 1 <= age <= 3:
        print("Varsta: {} ani - Baby".format(age))
    elif 4 <= age <= 9:
        print("Varsta: {} ani - Child".format(age))
    elif 10 <= age <= 15:
        print("Varsta: {} ani - Teenager".format(age))
    elif 16 <= age <= 18:
        print("Varsta: {} ani - Young".format(age))
    elif 19 <= age <= 50:
        print("Varsta: {} ani - Adult".format(age))
    else:
        print("Varsta: {} ani - Old".format(age))
