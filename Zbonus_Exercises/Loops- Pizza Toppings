#QUESTION:
"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza."""
#ANSWER:
toppings =[]
while True:
    USER_TOPPINGS = input("ENTER AS MANY TOPPINGS AS YOU WANT AND TYPE QUIT TO FINISH THE ORDER: ")

    if USER_TOPPINGS.lower() == 'quit':
        print("YOUR ORDER IS NOTED. PLEASE WAIT FOR YOUR TURN AND CHECK YOUR ORDER")
        if toppings:
            print("THIS IS YOUR FINAL ORDER")
            for topping in toppings:
                print(f"*{topping}")
        else:
            print("YOUR ORDOR HAS NO TOPPINGS")
        break
    else:
        toppings.append(USER_TOPPINGS)
        print(f"{USER_TOPPINGS} IS ADDED. PLEASE TYPE THE NEXT TOPPING.")
