def removeDupAtNthPos(lst, ele = None, occurance = None):
    occ_cnt, pos, freq = 0, 0, dict()
    for i in lst:
        if i == ele:
            occ_cnt += 1
            freq.update({(occ_cnt): [ele, pos]})
        pos += 1
    for key, val_list in freq.items():
        if key == occurance:
            ind = val_list[1]
    return ind

a = [1, 1, 2, 56, 0, 87, 2, 7, 56, 5, 2, 3, 56]
print("Given list: ", a)
ele = int(input("ENter the elemnt to be deleted:"))
occurance = int(input("At which occurance you want it to be deleted:"))
ind = removeDupAtNthPos(a, ele = ele, occurance = occurance)
print("Element to be deleted is:", a[ind], "at the index position:", ind, "for the occurance:", occurance)
a.pop(ind)
print("After the removal of nth occurance:", a)



