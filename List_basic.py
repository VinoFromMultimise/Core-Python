from copy import copy
from copy import deepcopy

# List - Complete walkthrough

# creating the List
x = 0
myList = [1, 2, 3, 4, 5, 10, "green"]       # using LIST literal
numbers = list(range(100))                  # using list() constructor

#accessing the elements
print('myList[0] = myList[-7] = ', myList[-7])          # elements can be accessed from index 0 to Length (positive - normal)
print('myList[6] = myList[-1] = ', myList[-1])          # elements can also be accessed from -1 to -length (negative - backwards)
print(numbers[99])                                      # In the range of 100 numbers, the 99th index position contains '100'

# traversing the elements 
for j in myList:
    print(j)

# traversing the range of 100 numbers and counting the multiples of 5
for k in numbers:
    if k % 5 == 0:
        x += 1 
print(x, 'number of multiples of 5 is in the range of 100 numbers')

# updating the elements in the list

myList[2] = "Heavens"

print(myList)

# creating alias of the list

a = [5, 10, 15, 20, 25]
newLst = a

print(newLst)

#update the new list and try printing the old one

newLst[3] = "Good day"

print(newLst)

# creating shallow copy of the list

countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

nations = countries.copy()    # nations = countries[:]

print("Address of nations: ", id(nations))
print("Address of countries: ", id(countries))

print("\n","Printing the address of countries")
for h in countries[:]:
    print(h, id(h))

print("\n","Printing the address of nations")
for t in nations[:]:
    print(t, id(t))

print((id(countries) == id(nations)))
print((id(nations[0]) == id(countries[0])))
print((id(nations[1]) == id(countries[1])))



