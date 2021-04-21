class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


a = SinglyLinkedList(1)
b = SinglyLinkedList(2)
c = SinglyLinkedList(3)

a.next_node = b
b.next_node = c


class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


a = SinglyLinkedList(1)
b = SinglyLinkedList(2)
c = SinglyLinkedList(3)

a.next_node = b
a.prev_node = None
b.next_node = c
b.prev_node = a
c.next_node = None
c.prev_node = b
