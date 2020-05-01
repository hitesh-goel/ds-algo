# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
class Node:
    def __init__(self, v, n=None):
        self.value = v
        self.next = n

    def print_ll(self):
        while self is not None:
            print(self.value)
            self = self.next


def reverse_sub_ll(head, p, q):
    p_temp = head
    q_temp = head
    temp = head

    while temp is not None:
        if temp.next == p:
            p_temp = temp
        if temp == q:
            q_temp = temp.next
        temp = temp.next
    previous = q_temp
    current = p
    next = None
    while next is not q_temp:
        next = current.next
        current.next = previous
        previous = current
        current = next

    p_temp.next = previous


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.print_ll()
    reverse_sub_ll(head, head.next, head.next.next.next)
    print("-- After Reversing --")
    head.print_ll()
    pass


if __name__ == '__main__':
    main()