## Exercise 10: Is it even? - 35 Marks
"""Write a program that tests if a value is even or odd. Follow the instructions outlined below:"""
### Instructions:
"""* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function."""
#DEFINITING A FUNTION TO CHECH IF THE FUNTION IS EVEN OR ODD
def EVEN_OR_ODD(NUMBER):
    #STATEMENT IF THE FUNTION IS EVEN
    if NUMBER %2 ==0:
        print(f"{NUMBER} IS EVEN")
    #STATEMENT IF THE FUNTION IS ODD
    else:
        print(f"{NUMBER} is ODD")

#DEFINING THE MAIN FUNTION AS PER THE REQUIRMENTS
def main_funtion():
    #TSKING USER INPUT
   NUMBER = int(input("ENTER A NUMBER TO CHECH IF ITS EVEN OF ODD: "))
   #FUNTION CALLING
   EVEN_OR_ODD(NUMBER)

if __name__ == "__main__":
    main_funtion()
