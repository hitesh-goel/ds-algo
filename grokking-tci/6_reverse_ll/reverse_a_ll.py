# Given Head of LL reverse the LL


class Node:
    def __init__(self, value, n=None):
        self.value = value
        self.next = n

    def print_ll(self):
        while self is not None:
            print(self.value)
            self = self.next


def reverse_ll(head):
    temp1 = head.next
    temp2 = temp1.next
    head.next = None
    while temp1 is not None:
        temp1.next = head
        head = temp1
        temp1 = temp2
        if temp2 is not None:
            temp2 = temp2.next
    head.print_ll()


def reverse_ll_2(head):
    current = head
    previous = None
    next = None
    while current is not None:
        previous = current
        current = current.next
        previous.next = next
        next = previous
    head.print_ll()


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.print_ll()
    reverse_ll(head)


if __name__ == '__main__':
    main()