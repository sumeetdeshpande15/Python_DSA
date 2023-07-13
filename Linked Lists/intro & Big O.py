'''
- Linked list do not have indexes.
- head points to the first node.
- tail points to the last node.
- each node points to the next node.
- last node points to None.
'''

''' LL BigO
- O(1) -> adding node to the end.
- O(n) -> removing an item from the end.
            - since LL works on pointers, once the last node is removed there is no direct pointer to the current last node apart from the second last node in the list. As a result, the only way is to iterate through the whole list and reach the last available node.
- O(1) -> adding an item at the beginning.
- O(1) -> removing an item from the beginning.
            - head = head.next()  points to the next node in the list.
- O(n) -> adding an item in between the list.
- O(n) -> removing an item from between the list.
- O(n) -> lookup in LL.
'''
