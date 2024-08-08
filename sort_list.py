a = [10, 0, -2, 1, 7, 100, 5, 8, 1]
print("Original list: ", a)


for j in range(0, len(a)):
    for k in range(j+1, len(a)):
        if a[j] >= a[k]:
            temp = a[j]
            a[j] = a[k]
            a[k] = temp
        
print(a)
                
