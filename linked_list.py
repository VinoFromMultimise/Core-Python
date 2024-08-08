# Appending to the list - completed
# Insert at a specific location - completed
# Printing and count of the nodes in a linked list - completed
# Delete from anywhere by mentioning either data, index or location - completed
# sort the linked list in a specific order - completed
# Find the extremities - Max and min node - completed
# Reversal of a linked list - completed
# Remove the duplicates from a linked list - completed
# Remove the nth occurance of a duplicate element in a linked list - completed
# Make an nth element to be present in an nth position - In Progress

# This linked list's data part deals with 'int' and 'float' type of data only
# Going further, I will update for 'str' type

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:

    del_items_list = []

    def __init__(self, head = None):
        self.head = head
    
    def __repr__(self):
        return self.head

    def appendToTheList(self, data):
        new_node = Node(data)

        # append to the last node
        if self.head != None:
            # assigning the head reference node to current_node here
            current_node = self.head

            # Traversing till the last available node. In the last node, the poniter will be None.
            while(current_node.next):
                current_node = current_node.next
            
            # After reaching last node, keep the reference of the newly created node into the last node's link part.
            current_node.next = new_node

        # if list is empty, make this as first node
        else:
            self.head = new_node
            return

    def insertAtSpecificLoc(self, data, loc):
        temp = self.head
        new_node = Node(data)

        if loc == 1:
            new_node.next = temp
            self.head = new_node
        else:    
            for i in range(1, loc):
                temp = temp.next

            new_node = Node(data)
            if temp:
                next = temp.next
                temp.next = new_node
                new_node.next = next      
            else:
                temp = new_node

    def removal(self, data_part, link_part, logic = None):
        #self.del_items_list.append(data_part)
        item = data_part
        link = link_part
        return link
    
    def removeNode(self, data_to_be_deleted = None, delete_at_index = None, delete_at_loc = None):
        temp = self.head
        if data_to_be_deleted != None:
            if data_to_be_deleted == temp.data:
                self.head = self.removal(temp.data, temp.next)
            else:
                while(temp):
                    if temp.data == data_to_be_deleted:
                        prev.next = self.removal(data_to_be_deleted, temp.next)
                        break
                    else:
                        prev = temp
                        temp = temp.next

        elif delete_at_index != None:
            if delete_at_index == 0:
                self.head = self.removal(temp.data, temp.next)
            else:
                act, stop_at = delete_at_index, delete_at_index + 1

                for i in range(stop_at):
                    if i == act:
                        prev.next = self.removal(temp.data, temp.next)
                    else:
                        prev = temp
                        temp = temp.next

        elif delete_at_loc:
            if delete_at_loc == 1:
                self.head = self.removal(temp.data, temp.next)
            else:
                act, stop_at = delete_at_loc, delete_at_loc + 1
                for i in range(1, stop_at):
                    if i == act:
                        prev.next = self.removal(temp.data, temp.next)
                    else:
                        prev = temp
                        temp = temp.next

    def printTheList(self):
        current_node = self.head
        count = 0
        while(current_node):
            print("|",current_node.data, "|-->", end = '')
            current_node = current_node.next
            count += 1
        print("None")
        #print("\n Number of nodes in the linked list:", count)
    
    def removeDupAtNthPos(self, lst, ele = None, occurance = None):
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
    
    def removeDups(self):
        hit_lst = []
        temp = self.head
        while(temp):
            hit_lst.append(temp.data)
            temp = temp.next
        act = linkedlist.removeDuplicatesInAList(hit_lst)
        print("These are the duplicate elements to be removed:", act)
        obj = linkedlist(self.head)
        for i in act[:]:
            obj.removeNode(data_to_be_deleted = i)
        obj.printTheList()

    def removeDuplicates(self):
        print("Do you want to remove the duplicates entirely or pop the nth occurance of a particular element??")
        print("1. Remove duplicates")
        print("2. Remove an element's nth occurance")
        print("Enter the option:")
        opt = int(input(''))
        obj = linkedlist(self.head)
        lst = []
        if opt == 1:
            obj.removeDups()
        else:
            ele = int(input("ENter the elemnt to be deleted:"))
            occurance = int(input("At which occurance you want it to be deleted:"))
            temp = self.head
            while(temp):
                lst.append(temp.data)
                temp = temp.next
            ind = obj.removeDupAtNthPos(lst, ele = ele, occurance = occurance)
            obj.removeNode(delete_at_index = ind)
        obj.printTheList()
        
    def reverseTheList(self):
        current = self.head
        next = prev = None
        while(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        h = prev
        while(h):
            print("|",h.data, "|-->", end = '')
            h = h.next
        print("None")
    
    def findMax(self):
        temp = self.head
        max = 0
        while(temp):
            if max < temp.data:
                max = temp.data
            temp = temp.next
        return max

    def findMin(self):
        t = self.head
        min= t.data
        t = t.next
        while(t):
            if t.data < min:
                min = t.data
            t = t.next
        return min
    
    def sortTheLinkedList(self, header_node):
        temp = header_node
        print("temp:", temp)
        lst = []
        while(temp):
            lst.append(temp.data)
            temp = temp.next
        print("original list:", lst)
        rev = linkedlist.sortList(lst)
        return f"The sorted list is : {rev}"
    
    @classmethod
    def sortList(cls, lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] >= lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst
    
    @classmethod
    def removeDuplicatesInAList(cls, lst):
        b = []
        lst.sort()
        print("Original list:", lst)
        length = len(lst[:])

        for j in range(0, length):
            temp = lst[j]
            for i in range(j+1, length):
                if temp == lst[i]:
                    b.append(lst[i])
        return b
    
e1 = linkedlist()
print("Appending into lists")
e1.appendToTheList(100)
e1.appendToTheList(20)
e1.appendToTheList(40)
e1.appendToTheList(40)
e1.appendToTheList(-2)
e1.appendToTheList(-2)
e1.appendToTheList(100)
e1.insertAtSpecificLoc(70, 1)
e1.printTheList()
#print("The maximum node is :", e1.findMax())
#print("The minimum node is :", e1.findMin())
#print("Reversing the list")
#e1.reverseTheList()
print("Remove duplicates")
e1.removeDuplicates()
head = e1.__repr__()
print(e1.sortTheLinkedList(head))



