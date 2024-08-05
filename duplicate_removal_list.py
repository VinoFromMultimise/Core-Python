a = [1, 1, 2, 56, 0, 87, 2, 7, 56]
b = []
a.sort()
print("Original list:", a)
length = len(a[:])

for j in range(0, length):
    temp = a[j]
    for i in range(j+1, length):
        if temp == a[i]:
            b.append(a[i])

for k in b:
    temp = k
    for i in a[:]:
        if i == temp:
            a.remove(temp)

unique_lst = a + b
unique_lst.sort()
print("Removed duplicates: ", unique_lst)

