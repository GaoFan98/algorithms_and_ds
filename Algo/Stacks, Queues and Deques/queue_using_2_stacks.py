class Queue2Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, el):
        self.instack.append(el)

    def dequeue(self):
        # if already not in outstack
        if not self.outstack:
            # do while instack becomes empty
            while self.instack:
                # append to outstack from the last element of instack
                # so the reversed version of instack
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()
