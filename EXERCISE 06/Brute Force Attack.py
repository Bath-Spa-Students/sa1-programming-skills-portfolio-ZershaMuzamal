"""## Exercise 6: Brute Force Attack - 30 MarksWrite a program that simulates a password entry system. The correct password is defined
as 12345. The program should keep asking the user to enter the password until they provide the correct one.
### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.
### Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the
remaining attempts. If the maximum number of attempts is reached,inform the user that the authorities have been alerted."""
#CREATING A PASSWORD
PASSWORD = "12345"

#USING WHILE LOOP FOR INFINITY LOOPS 
while True:
    #ASKING USER TO ENTER PASSWORD TO CHECK
    ENTERED_PASSWORD = input("ENTER THE CORRECT PASSWORD FOR ACCESS:")
    #CHECKING IF THE ENTERED PASSORD MATCHES TO THE REAL PASSWORD
    if ENTERED_PASSWORD == PASSWORD:
        #IF THE PASSWORD IS CORRECT THIS PRINT STATEMENT WILL PRINT AND LOOP WILL END BECAUSE OF BREAK
        print("ACCESS GRANTED!!")
        break
    #IF THE PASSWORD IS WRONG THE LOOP WILL CONTINUE PRINTING THIS STATEMENT
    else:
        print("WRONG PASSWORD, TRY AGAIN.")
