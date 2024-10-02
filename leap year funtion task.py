"""
TASK:-
determine whether the given year is leap year or not by return Boolean True; otherwise, return False:
   1)The year can be evenly divided by 4. If it is an even number of hundreds:
   2.1)The year is also evenly divisible by 100, then it is NOT a leap year; unless:
       2.2) The year can be evenly divided by 400. A leap year, unless:

Constraints:
   1900<=year<= 10**5
   code must use functions
"""

def is_leap(year):

    while (10**5)>= year >=1900 :

        if year % 100 == 0 and year % 400 == 0:
            return("True")
              
               
        elif year % 100 != 0 and year % 400 != 0 and  year % 4 == 0 :
            return ("True")

        else :
            return("False")
       

year = int(input())
print(is_leap(year))


