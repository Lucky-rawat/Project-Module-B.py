class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtEnd(2)
    llist.insertAtEnd(3)
    llist.insertAtEnd(4)
    print('linked list:')
    llist.printList()
    llist.insertAtEnd(22)
    print('\nlinked list after inserting another element at the end:')
    llist.printList()
