class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def reverse(self, head):
        prev = None
        curr = head

        while curr is not None:
            next_temp = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next_temp

        return prev
