#Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
#A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
#If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
#Implement the MyLinkedList class:
#MyLinkedList() Initializes the MyLinkedList object.
#int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
#void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#void addAtTail(int val) Append a node of value val as the last element of the linked list.
#void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
#void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
#Example 1:
#Input
#["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
#[[], [1], [3], [1, 2], [1], [1], [1]]
#Output
#[null, null, null, null, 2, null, 3]
#Explanation
#MyLinkedList myLinkedList = new MyLinkedList();
#myLinkedList.addAtHead(1);
#myLinkedList.addAtTail(3);
#myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
#myLinkedList.get(1);              // return 2
#myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
#myLinkedList.get(1);              // return 3

class MyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.length:
            return
        current = self.head
        if index <= 0:
            self.head=MyNode(val, self.head)
        else:
            for i in range(index - 1):
                current = current.next
            current.next=MyNode(val, current.next)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1
