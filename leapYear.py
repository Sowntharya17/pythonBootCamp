year=2024
# If a number divisible by 4, it is a leap year. If not it's not a leap year.
# If a number divisible by 4 and also by 100, it must be divisible by 400.
# If a number divisible by 4 and 100, but not by 400. Ir is not leap year.
'''
if ((year%4==0 and year%100!=0) or (year%400==0)):
    print("It is a Leap year")
else:
    print("It is not a Leap year")
'''

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")