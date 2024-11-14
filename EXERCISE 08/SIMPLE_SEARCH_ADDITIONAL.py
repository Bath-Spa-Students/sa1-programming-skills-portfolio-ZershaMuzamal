## Exercise 8: Simple Search - 30 Marks
"""Write a program that searches for a specific string within a list of strings. 
The list is initialized with specific names
("Jake","Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam"."""
# Optional Requirements:
"""1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""

#CREATING A LIST
NAMES_LIST =["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#TAKING USER INPUT TO CHECK IF TH INPUT IS IN THE LIST
ENTERED_NAME = input("ENTER A NAME TO CHECK IF IT IS IN THE LIST:")
#ADDING IF-ELSE STATEMENT FOR CONDITIONS
if ENTERED_NAME.lower() in [name.lower() for name in NAMES_LIST]:
    #ADDING INDEX FUNTION TO CHECK TH LIST
    index = [name.lower() for name in NAMES_LIST].index(ENTERED_NAME.lower())
    #PRINT STATEMENT IF THE CONDITION IS TRUE
    print(f"THE NAME ENTERED IS AT INDEX {index} IS THE LIST")
else:
    #PRINT STATEMENT IF THE CONDITION IS FALSE
    print("THE NAME ENTERED IS NOT IN THE LIST")
