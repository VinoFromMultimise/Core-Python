# Appending to the list
# Insert at a specific location
# Printing and count of the nodes in a linked list
# Delete from anywhere by mentioning either data, index or location
# sort the linked list in a specific order
# Find the extremities - Max and min node
# Reversal of a linked list
# Remove the duplicates from a linked list
# Remove the nth occurance of a duplicate element in a linked list
# Make an nth element to be present in an nth position

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:

    del_items_list = []

    def __init__(self, head = None):
        self.head = head

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
        link = None
        self.del_items_list.append(data_part)
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
        print("\n Number of nodes in the linked list:", count)

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
    
e1 = linkedlist()
print("Appending into lists")
e1.appendToTheList(100)
e1.appendToTheList(20)
e1.appendToTheList(3)
e1.appendToTheList(40)
e1.appendToTheList(-2)
e1.printTheList()
print("Inserting at specific location")
e1.insertAtSpecificLoc(40,1)
e1.printTheList()
print("Removing en element from the list")
e1.removeNode(data_to_be_deleted = 40)
e1.printTheList()
print("The maximum node is :", e1.findMax())
print("The minimum node is :", e1.findMin())
