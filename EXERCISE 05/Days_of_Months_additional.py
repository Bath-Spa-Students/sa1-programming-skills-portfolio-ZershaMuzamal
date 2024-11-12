## Exercise 5: Days of the Month - 30 Marks
"""Write a program that tells a user how many days there are in a specific month. Use a dictionary to 
map the month numbers (1-12) to the number of days in each month.
### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are
the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number
of days in the corresponding month."""
### Advanced Requirement:
"""Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user
if the year is a leap year and adjust the number of days accordingly."""
month_days = {
#JUNUARY     
1: 31,
#FEBURARY (ASUMED AS NON LEAP-YEAR)
2: 28,
#MARCH
3: 31,
#APRIL
4: 30,
#MAY
5: 31,
#JUNE    
6: 30,
#JULY
7: 31,
#AUGUST
8: 31,   
#SEPTEMBER  
9: 30,
#OCTOBER      
10: 31,
#NOVEMBER  
11: 30,
#DECEMBER  
12: 31  
}
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

#ASKING FOR USER INPUT OF MONTH
INPUT_NUMBER = int(input("ENTER A MONTH NUMBER BETWEEN (1-12):"))
#USING IF ELSE STATEMENT FOR CREATING CONDITIONS
if 1 <= INPUT_NUMBER <= 12:
   #IF USER ENTER 2 (FEBURARY) WE WILL DEAL IT DIFFRENTLY
    if INPUT_NUMBER == 2:
        #WE WILL ASK FOR YEAR
        year= int(input("ENTER THE YEAR PLEASE:"))
        #IF THE USER ENTER A LEAP YEAR FOLLOING CONDITIONS WILL BE FOLLOWED 
        if is_leap_year(year):
            print(f"ACCORDING TO THE ENTERED YEAR {year} FEBURARY HAS 29 DAYS AS ITS A LEAP YEAR ")
        #IF USER ENTER A NON LEAP YEAR FOLLOWING CONDITIONS WILL BE FOLLOWED 
        else:
            print(f"ACCORDING TO THE ENTERED YEAR {year} FUBURARY HAS 28 DAYS AS ITS A NON LEAP YEAR") 
    #PRINT STATEMENT IF THE CONDITION IS FULLFILLEd
    else:
     print(f"The number of days in month {INPUT_NUMBER} is {month_days[INPUT_NUMBER]}.")
#PRINT STATEMENT IF THE COONDITION IS NOT FULLFILLED
else:
    print("INVALIDE MONTH NUMBER PLEASE CHOSE BETWEEN (1-12)")
