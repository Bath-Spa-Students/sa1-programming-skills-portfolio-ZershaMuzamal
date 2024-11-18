#HOMOGENEOUS LIST

#LIST 1
Falak_Grocery_List = ["Chocolates" , "Cake" , "Drinks" , "Jam"]
#PRINTING THE LIST 
print(Falak_Grocery_List)


#LIST 2
Friends_List = ["ABBIA" , "FALAK" , "AMBREEN"]
#PRINTING THE LIST
print(Friends_List)


#position of each element
numbers = [10,20,30,40,50]
print("first element:", numbers[0])


#changing a element of list
animals = ["bird" , "dog" , "hen"]
animals[1] = "falak"
print(animals)


#add new values in the list 
colors=[]
colors.append("red")
print(colors)


#remove a value from the list
coloors = ["red" , "pink" , "orange"]
coloors.remove("red")
print(coloors)


#sum of numbers in a list
NUMBERS = [6 , 7 , 8 , 9]
TOTAL = sum(NUMBERS)
print(TOTAL)

#MINIMUM AND MAXIMUM VALUE
ages = [23 , 54 , 58 , 78 ]
print("minimum age:", min(ages))
print("maximum age:", max(ages))


#sort the list

#check if the elemt exist in the list
num = [1, 2, 3, 4, 5]
if 5 in num:
    print("yes")
else:
    print("no")


#count occurence of an element
items = [1,1,1,2,2,2,4,4,4,4]
count_of_4 = items.count(4)
print(count_of_4)

#extand of list
list1 = [1 , 2 , 3]
list2 = [4 , 5 ]
list1.extend(list2)
print(list1)


#HETROGENEOUS LIST

#LIST 1
Personal_Information = ["ZERSHA_MUZAMAL" , 2005 , 97.7]
#PRINTING THE LIST
print(Personal_Information)

#LIST 2
Passport_Components =  ["fatima_muzamal" , 3743892347 , 345.9, ]
#PRINTHIN THE LIST
print(Passport_Components)
