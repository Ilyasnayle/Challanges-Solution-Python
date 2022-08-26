def LinkedList():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    class LinkedList:
        def __init__(self):
            self.head = None
        def append(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        def display(self):
            curr = self.head
            while curr:
                print(curr.data, end = ' ')
                curr = curr.next
            print()
        def remove(self, data):
            if self.head.data == data:
                self.head = self.head.next
                return
            curr = self.head
            while curr.next:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return
                curr = curr.next
    return LinkedList()
def main():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.display()
    ll.remove(3)
    ll.display()
if __name__ == '__main__':
    main()
