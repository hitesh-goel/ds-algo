# find the shortest path in graph from one node to another node
# provided graph is represented in adjacency list

from collections import deque

queue = []

def bks(ntw, start, end):

    if end in queue:
        return 'found'
    else:
        queue.extend(ntw[start])
        # dequeue
        bks(ntw, deq, end)


# 1 get the list of friends start connected to
# 2 check if any of them is the end
# 3 if any of them is end then say found
# 4 else remove first friend from the queue and add it's friends to the queue
# repeat from 2 till 4


def test():
    network = {
        'Min': ['William', 'Jayden', 'Omar'],
        'William': ['Min', 'Noam'],
        'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
        'Ren': ['Jayden', 'Omar'],
        'Amelia': ['Jayden', 'Adam', 'Miguel'],
        'Adam': ['Amelia', 'Miguel'],
        'Miguel': ['Amelia', 'Adam'],
        'Noam': ['Jayden', 'William'],
        'Omar': ['Ren', 'Min'],
        'hitesh': ['Ren']
    }

    assert(bfs(network, 'Min', 'Noam')) == ['Min', 'William', 'Noam']
    assert(bfs(network, 'Min', 'hitesh')) == []


test()
