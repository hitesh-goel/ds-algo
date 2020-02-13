# Given 2 strings validate other is permutation of the first one

# Solutions
# 1. Bruteforce check for each value and maintain the indexes in the 2nd one if that index is already checked or not
# 2. Create 2 hashmaps if both hashmaps are same it means strings are palindromes
# 3. Sort both of the strings and then just check if both strings match or not.

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    map1 = {}
    map2 = {}

    for k in str1:
        if map1.get(k, "") != "":
            map1[k] += 1
        else:
            map1[k] = 1

    for k in str2:
        if map2.get(k, "") != "":
            map2[k] += 1
        else:
            map2[k] = 1

    return map1 == map2

def main():
    str1 = "abcda"
    str2 = "bcdaa"
    assert(check_permutation(str1, str2)) == True

if __name__ == "__main__":
    main()
