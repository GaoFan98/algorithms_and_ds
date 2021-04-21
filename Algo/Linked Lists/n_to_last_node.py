class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def nth_to_last_node(self, n, head):
        left_pointer = right_pointer = head

        for i in range(n - 1):
            if not right_pointer.next_node:
                raise LookupError('n is larger than liked list')

            right_pointer = right_pointer.next_node

        while right_pointer.next_node:
            left_pointer = left_pointer.next_node
            right_pointer = right_pointer.next_node

        return left_pointer
