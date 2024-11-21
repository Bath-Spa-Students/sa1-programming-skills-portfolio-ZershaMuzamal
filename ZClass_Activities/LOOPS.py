#WHILE LOOP 

#JUST A WHILE LOOP
num = 1
while num<= 10:
    print("NUMBER IS: " , num)
    num += 1


#WHILE LOOP WITH BREAK STATEMENT AND IF
age = 19
while age<=20:
    print("YOU ARE STILL YOUNG")
    if age == 10:
      print("HALF WAY TO GO" , age)
    break
   
#WHILE LOOP WITH CINTINUE STATEMENT AND IF
NUMB = 0
while NUMB < 6:
  NUMB += 1
  if NUMB == 3:
    continue
  print("NUMBER IS : ",NUMB)

#WHILE LOOP WITH A ELSE STATEMENT
number = 1
while number < 6:
  print("NUMBER IS : " ,number)
  number += 1
else:
  print("NUMBER IS GREATER THAN 6")


#FOR LOOP

#FOR LOOP PRINTING EACH VALE IN A WORD
for ALPHABET in "APPLE" :
   print(ALPHABET)

#FOR LOOP PRINTING EACH VALUE AT A TIME 
FRUITS = ["APPLE", "BANANA", "MANGO"]
for fruit in FRUITS:
  print(fruit) 

#FOR LOOP PRINTING EACH VALUE AT A TIME TILL THE BREAK STATEMENT
FRUITS = ["APPLE", "BANANA", "MANGO"]
for fruit in FRUITS:
  if fruit == "BANANA":
   break
  print(fruit)

#FOR LOOP PRINTING A RANGE
for NUMBERR in range(6):
  print(NUMBERR) 
else:
  print("THE COUNT ENDS HERE!!")
