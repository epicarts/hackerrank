#-*- coding: utf-8 -*-
#python3
#Gregorian clendar 윤년계산


year = int(input())
print(is_leap(year))

def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 is 0 and year % 100 is not 0 or year % 400 is 0:
        leap = True

    return leap

