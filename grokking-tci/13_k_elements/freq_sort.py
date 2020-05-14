# Given a string, sort it based on the decreasing frequency of its characters.
#
# Example 1:
#
# Input: "Programming"
# Output: "rrggmmPiano"
# Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
#
# Example 2:
#
# Input: "abcbab"
# Output: "bbbaac"
# Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
from heapq import *


def freq_sort(letters):
    d, arr = {}, list(letters)
    for l in arr:
        d[l] = d.get(l, 0) + 1

    h = []
    for l, i in d.items():
        heappush(h, (-i, l))

    r = ""
    while len(h) > 0:
        t, i = heappop(h), 0
        while i < -t[0]:
            r = r + t[1]
            i += 1

    return r


def main():
    assert freq_sort("abcbab") == "bbbaac"
    pass


if __name__ == '__main__':
    main()