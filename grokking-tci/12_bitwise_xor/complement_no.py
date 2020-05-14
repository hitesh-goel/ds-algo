# Every non-negative integer N has a binary representation,
# for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.
#
# The complement of a binary representation is the number in binary
# that we get when we change every 1 to a 0 and every 0 to a 1.
# For example, the binary complement of “1010” is “0101”.
#
# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.


def complement_no(no):
    rmb = 1

    for _ in range(int.bit_length(no)):
        no ^= rmb
        rmb = rmb << 1

    return no


def main():
    assert(complement_no(10) == 5)
    assert(complement_no(8) == 7)

    n, c = 30, 0

    while n > 0:
        t = n
        n = n >> 2
        c += 1
        print(t, ' = ', bin(t)[2:], ' => ', bin(n)[2:], ': ', c)
    pass


if __name__ == '__main__':
    main()