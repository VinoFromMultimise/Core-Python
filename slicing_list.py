# Slicing of the list

# Syntax -> list_object[start:stop:step]

#create a list

a = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(a)

print(a[-4])
print(a[4])
print(a[-4:])
print(a[-4:-2])

# Just print the list
print(a)

# Print only even numbers
print(a[1::2])

# print only odd numbers
print(a[0::2])

# as the starting position doesn't change, just step up to 2 to get odd numbers
print(a[::2])

# print the list using sliceing
print(a[:])
print(a[::])

# get the middle four
print(a[3:7]) 

# get the first three even numbers
print(a[1:6:2])

# get the first three even numbers - use negative indexing
print(a[-9:6:2])

# get the first three odd numbers - use negative indexing
print(a[:6:2])

# If start is before the beginning of the list, which can happen when you use negative indices, then Python will use 0 instead.
print(a[-11:2])
print(a[-11:1])
print(a[-100:2])

# If start is greater than stop, then the slicing will return an empty list.
print(a[1:-10])

# If stop is beyond the length of the list, then Python will use the length of the list instead.
print(a[:11])

# print the list in reverse way - negative value to step counter
print(a[::-1])
print(a[::-2])
print(a[::-3])
print(a[::-4])
print(a[1::-4])
