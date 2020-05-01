# https://www.interviewcake.com/question/python3/largest-stack


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStackClass(object):

    def __init__(self):
        self.max_el_stack = Stack()
        self.stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if item > self.max_el_stack.peek():
            self.max_el_stack.push(item)

    def pop(self):
        res = self.stack.pop()
        if res == self.max_el_stack.peek():
            self.max_el_stack.pop()
        return res

    def get_max(self):
        return self.max_el_stack.peek()


def main():
    max_stack = MaxStackClass()
    max_stack
    pass


if __name__ == '__main__':
    main()