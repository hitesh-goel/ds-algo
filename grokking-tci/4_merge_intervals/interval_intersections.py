# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

class Interval():
    def __init__(self, s, e):
        self.s = s
        self.e = e
    
    def print_interval(self):
        print('[', self.s, ',', self.e, ']')

def intervals_intersection(intervals_1, intervals_2):
    intersections = []
    i1, i2 = 0, 0
    li1 = len(intervals_1)
    li2 = len(intervals_2)
    while i1 < li1 and i2 < li2:
        s = intervals_1[i1].s
        e = intervals_1[i1].e
        s2 = intervals_2[i2].s
        e2 = intervals_2[i2].e
        
        if s <= s2 <= e or s2 <= s <= e2:
            intersections.append(Interval(max(s, s2), min(e2, e)))
        if e < e2:
            i1 += 1
        else:
            i2 += 1
    return intersections  

def main():
    ints = intervals_intersection([Interval(1,3), Interval(5,6), Interval(7,9)], [Interval(2,3), Interval(5,7)])
    for i in ints:
        i.print_interval()
    print('======')
    ints = intervals_intersection([Interval(1,3), Interval(5,7), Interval(9,12)], [Interval(5,10)])
    for i in ints:
        i.print_interval()

if __name__ == '__main__':
    main()
