class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head
        steps = 0
        while curr:
            if steps == index:
                return curr.item
            curr = curr.next
            steps += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        curr = self.head
        steps = 0
        while curr and steps < index - 1:
            curr = curr.next
            steps += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node
        # else index > list length -> do nothing

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        steps = 0
        while curr and steps < index - 1:
            curr = curr.next
            steps += 1
        if curr and curr.next:
            curr.next = curr.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)