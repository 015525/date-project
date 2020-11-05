print ("This is a programme to check the vadility of dates\n")
x=0
try :
    year = int(input("please enter a year : "))
    month = int(input("please enter a month : "))
    day = int(input("please enter a day : "))
except :
    print ("invalid input")
else :
    if year > 2020 or year < 0:
        print("invalid year")
        x=1
    if year % 4 == 0:
        print("leap year يعني سنة كبيسة")
    if month > 12 or month < 0:
        print("invalid month")
        x = 1
    if day > 31 or day < 0:
        print("invalid day")
        x = 1
    else :
        if month == 2:
            if year % 4 == 0 :
                if day > 29 or day < 0:
                    print("invalid day in this month")
                    x = 1
            elif day > 28 or day < 0:
                print("invalid day in this month")
                x = 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31 or day < 0:
                print("invalid day in this month")
                x = 1
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30 or day < 0:
                print("invalid day in this month")
                x = 1
if x== 0 :
    print ("valid date")




