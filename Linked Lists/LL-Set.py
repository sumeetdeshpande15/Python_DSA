class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    # Alternate solution for Set Value
    def set_value_alt(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        

ll = LinkedList(2)
ll.append(7)
ll.append(98)
ll.append(3)
ll.append(4)
ll.print_list()
print()
ll.set_value_alt(2,66)
ll.print_list()