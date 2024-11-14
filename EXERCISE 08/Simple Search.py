## Exercise 8: Simple Search - 30 Marks
"""Write a program that searches for a specific string within a list of strings. 
The list is initialized with specific names
("Jake","Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam"."""
# Optional Requirements:
"""1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input."""

#CREATING A LIST
NAMES_LIST =["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#INITIALIZING A A SPECIFIC NAME
ENTERED_NAME = "Sam"
#ADDING IF-ELSE STATEMENT FOR CONDITIONS
if ENTERED_NAME in NAMES_LIST:
    #PRINT STATEMENT IF THE CONDITION IS TRUE
    print("SAM IS IN THE LIST")
else:
    #PRINT STATEMENT IF THE CONDITION IS FALSE
    print("SAM IS NOT IN THE LIST")
