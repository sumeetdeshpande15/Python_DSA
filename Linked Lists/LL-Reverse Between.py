'''
You are given a singly linked list and two integers m and n. Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

Input

* The method reverse_between takes two integer inputs m and n.

* The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)

Output

* The method should modify the linked list in-place by reversing the nodes from index m to index n.

* If the linked list is empty or has only one node, the method should return None.


Example

* Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0


    def reverse_between(self, m, n):
        if self.length <= 1:
            return 
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(m):
            prev = prev.next

        current = prev.next

        for _ in range(n-m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        self.head = dummy.next



linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()
