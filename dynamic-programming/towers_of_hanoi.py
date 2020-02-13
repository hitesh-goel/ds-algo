# transfer all the nodes in a tower to last tower


class Tower:
    def __init__(self, id):
        self.id = id
        self.blocks = []

    def print_tower(self):
        print("Tower: {} with values: {}".format(self.id, self.blocks))

    def add(self, val):
        self.blocks.append(val)

    def remove(self):
        # TODO(1): handle empty no of blocks
        return self.blocks.pop()


def transfer(n, source, dest, buffer):
    if n == 0:
        return
    transfer(n-1, source, buffer, dest)
    move(n, source, dest, buffer)
    transfer(n-1, buffer, dest, source)


def move(block, source, dest, buffer):
    source.print_tower()
    dest.print_tower()
    buffer.print_tower()
    val = source.remove()
    dest.add(val)


def main():
    t1 = Tower('A')
    t2 = Tower('B')
    t3 = Tower('C')

    i, v = 4, 4
    while i > 0:
        t1.add(i)
        i -= 1

    print('before transfer')
    t1.print_tower()
    t2.print_tower()
    t3.print_tower()
    print('==========start in btw transfer states==========')
    transfer(v, t1, t3, t2)
    print('==========end in btw transfer states==========')
    print('after transfer')
    t1.print_tower()
    t2.print_tower()
    t3.print_tower()


main()
