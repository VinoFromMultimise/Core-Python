# Working with the List methods

# create a new list
animals = ['dog', 'cat']

# append() : adds an element to the end of the list.						.append(item)
animals.append('cow')
animals.append('Bull')						# animals[len(animals):] = ["hawk"]

print(animals)

# extend() : extends the list by appending elements from another iterable.			.extend([iterables])
animals.extend(['Goat', 'pigs', 'dragons'])			# animals[len(animals):] = ['Goat', 'pigs', 'dragons']

print(animals)

# insert() : adds an element at a specified position in the list. 				.insert(index, item)
animals.insert(5, 'Hens')         				# list_object[index:index] = [item]

# remove() : removes the first occurrence of a specified element from the list.		 	.remove(item)
animals.remove("pigs")	

print(animals)

# pop()    : removes the element at a specified position in the list and returns it. 		.pop([index])	
animals.pop()
print(animals)

animals.pop(0)
animals.pop(-1)

print(animals)

# sort()   : sorts the elements in the list in ascending order.


# reverse(): reverses the order of the elements in the list.
# It’s important to note that reversed() retrieves items from the input sequence lazily. This means that if something changes in the input sequence during the reversing # # process, then those changes will reflect in the final result.

g = reveresed(animals)
print(type(g))
print(list(g))

# count()  : returns the number of times a specified element appears in the list.
cnt = animals.count()
print("count of animals in farm: ", cnt)

animals.append("cows")
cnt_cows = animals.count("cows")
print("count of cows in farm: ", cnt_cows)

# index()  : returns the index of the first occurrence of a specified element in the list.
pos = animals.index("Bull")
print(pos)

# clear : Remove all the items in one go.								.clear()
animals.clear() 						# animals[:] = []	

