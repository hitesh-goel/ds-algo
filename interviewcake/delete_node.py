# Delete the node of a single linked list. Where you got reference to the node only.


class LinkedListNode(object):

    def init(self, value):
        self.next = None
        self.value = value

def delete_node(node):
    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

delete_node(b)
