class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    p1, p2 = head, head.next.next
    while p2 != None and p2.next != None:
        if p1 == p2:
            return True
        p1 = p1.next
        p2 = p2.next.next
    return False

def length_of_cycle(head):
    p1, p2 = head, head.next.next
    while p2 != None and p2.next != None: 
        if p1 == p2:
            break
        p1 = p1.next
        p2 = p2.next.next
    if p1 == p2:
        p2 = p1.next
        l = 1
        while p1 != p2:
            l += 1
            p2 = p2.next
        return l
    else:
        return 0

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    assert(has_cycle(head) == False)

    head.next.next.next.next.next.next = head.next.next
    assert(has_cycle(head) == True)

    assert(length_of_cycle(head)== 4)
    
if __name__ == '__main__':
    main()
