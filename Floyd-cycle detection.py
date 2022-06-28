class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp


    def detectCycle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while (fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False


mylist = LinkedList()
values = [20, 30, 40, 50, 60]
n = len(values)
for i in range(n - 1, -1, -1):
    mylist.insert(values[i])

mylist.head.next.next.next.next = mylist.head.next
if mylist.detectCycle():
    print("Cycle found")
else:
    print("No cycle found")