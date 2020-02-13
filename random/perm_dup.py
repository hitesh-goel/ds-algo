# return permutations of a string if duplicates are there


def permutations(map, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return
    for key in map.keys():
        count = map[key]
        if count > 0:
            map[key] = count - 1
            permutations(map, prefix + key, remaining - 1, result)
            map[key] = count


def main():
    map = {'a': 2, 'b': 1}
    result = []
    permutations(map, "", 3, result)
    print(result)


main()
