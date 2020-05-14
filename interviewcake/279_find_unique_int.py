# https://www.interviewcake.com/question/python3/find-unique-int-among-duplicates

# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.


def find_unique_int(arr):
    ui = 0
    for no in arr:
        ui = ui ^ no
    return ui


def main():
    assert find_unique_int([1,2,3,4,5,5,4,3,1]) == 2


if __name__ == '__main__':
    main()