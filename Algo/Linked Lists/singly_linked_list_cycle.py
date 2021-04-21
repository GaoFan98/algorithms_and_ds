class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def cycle_check(self, node):
        if node is None:
            return False

        slow = fast = node

        while slow != fast:
            if fast.next_node is None or fast.next_node.next_node is None:
                return False

            slow = slow.next_node
            fast = fast.next_node.next_node

        return True
