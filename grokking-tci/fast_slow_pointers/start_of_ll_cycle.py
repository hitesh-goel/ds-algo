class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start_point(head):
    
    return head.value

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    assert(cycle_start_point(head) == 3) 

if __name__ == '__main__':
    imain()




