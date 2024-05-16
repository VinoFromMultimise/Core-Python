from copy import copy
from copy import deepcopy

def copy_fun(method,lst):
    
    if method == 1:
        newlst = lst
        print("Illustartion of Aliasing--------------")
    elif method == 2:
        newlst = copy(lst)
        print("Illustartion of Shallow copying--------------")
    elif method == 3:
        newlst = deepcopy(lst)
        print("Illustartion of Deep copying--------------")
    else:
        print("go home, nothing is copied, check the below error")
        
    print("old: ", lst)
    print("copied: ", newlst)
    print()
    for i in range(len(lst)):
        print("\"",lst[i],"\""," of old list is at: ",id(lst[i]))
        print("\"",newlst[i],"\""," of copied list is at: ",id(newlst[i]))
        print("*-----------------------------------------------------------*")
    
    print("\n changing the assignment after copying:")
    print("^^^^^^Check the reflection in the copied list^^^^^^")
    lst[3] = "vinodhini"
    print("old: ", lst)
    print("copied: ", newlst)
    print()
    
    print("\"",lst[3],"\""," of old list is at: ",id(lst[3]))
    print("\"",newlst[3],"\""," of copied list is at: ",id(newlst[3]))
    print("*-----------------------------------------------------------*")

        
lst1 = ["Land", "of", "Wonders", "is", "awaiting", (1, 2, 3), [60, 70]]
print("Illustartion of copying method in Multimise:")
print("\n*---Choose the method # you want to learn---*")
print("1. Aliasing", "2. Shallow copying", "3. Deep copying", sep = '\n')
method_num_chosen = int(input())
copy_fun(method_num_chosen, lst1)


