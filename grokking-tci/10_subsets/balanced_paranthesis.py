# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
from collections import deque


class ParathesisString:
    def __init__(self, p_str, oc, cc):
        self.p_str = p_str
        self.oc = oc
        self.cc = cc


def balanced_pars(no):
    if no == 0:
        return []

    balanced_pairs = deque()
    balanced_pairs.append(ParathesisString("(", 1, 0))
    result = []

    while balanced_pairs:
        el = balanced_pairs.popleft()
        # add when oc & cc are = n
        if el.oc == no and el.cc == no:
            result.append(el.p_str)

        # add ) at another step
        if el.cc <= no and el.cc < el.oc:
            p_str  = el.p_str + ')'
            balanced_pairs.append(ParathesisString(p_str, el.oc, el.cc + 1))

        # add ( at one step
        if el.oc <= no:
            p_str  = el.p_str + '('
            balanced_pairs.append(ParathesisString(p_str, el.oc + 1, el.cc))

    return result


def main():
    print(balanced_pars(2))
    print(balanced_pars(3))
    print(balanced_pars(4))
    pass


if __name__ == '__main__':
    main()