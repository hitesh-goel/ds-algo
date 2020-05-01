# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
class Node:
    def __init__(self, v, n=None):
        self.value = v
        self.next = n

    def print_ll(self):
        while self is not None:
            print(self.value)
            self = self.next


def reverse_ll(p, q):
    pass


def reverse_every_k_sub_ll(head, k):
    current = head
    temp = head
    previous = head.next
    next = current.next
    i = 1
    while i < k:
        head = head.next
        i += 1
    i = 0
    while current is not None:
        if i == 0:
            temp.next = previous
            previous = current
            while i < k:
                previous = previous.next
                i += 1
        print('here')
        head.print_ll()
        current.next = previous
        previous = current
        current = next
        next = next.next
        i -= 1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.print_ll()
    reverse_every_k_sub_ll(head, 3)
    print("-- After Reversing --")
    head.print_ll()
    pass


if __name__ == '__main__':
    main()