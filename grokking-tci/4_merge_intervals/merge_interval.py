# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

class interval():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print('[' + str(self.start) + ',' + str(self.end) + ']')

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end
    
    merged_intervals = []
    for key in range(1, len(intervals)):
        if intervals[key].start < end:
            end = max(intervals[key].end, end)
        else:
            merged_intervals.append(interval(start, end))
            start = intervals[key].start
            end = intervals[key].end
    merged_intervals.append(interval(start,end)) 
    return merged_intervals

def main():
    for i in merge_intervals([interval(1,4), interval(2,5), interval(7,9)]):
        i.print_interval()

if __name__ == '__main__':
    main()
