# ineert a given interval at the correct position and merge all necessary intervals to produce a list

class Interval():
    def __init__(self, s, e):
        self.s = s
        self.e = e
    
    def print_intervals(self):
        print('[' + str(self.s) + ',' + str(self.e) + ']')

def insert_interval(intervals, interval):
    merged = []
    i = 0

    while i < len(intervals) and intervals[i].e < interval.s:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i].s < interval.e:
        interval.s = min(intervals[i].s, interval.s)
        interval.e = max(intervals[i].e, interval.e)
        i += 1

    merged.append(interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged

def main():
    intervals = insert_interval([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,6))
    for i in intervals:
        i.print_intervals()
    print('======') 
    intervals = insert_interval([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4, 10))
    for i in intervals:
        i.print_intervals()
    print('======') 
    intervals = insert_interval([Interval(2,3), Interval(5,7)], Interval(1, 4))
    for i in intervals:
        i.print_intervals()


if __name__ == '__main__':
    main()
