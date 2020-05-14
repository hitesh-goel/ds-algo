# https://www.interviewcake.com/question/python3/cake-thief


def max_duffel_bag_value(cakes, capacity):

    max_val_at_cap = [0]*(capacity+1)

    # sort the cakes on the basis of weight
    # calculate max duffel bag value at each weight till max capacity reaches
    # max_value = cake_value + max_val_at_cap(capacity-cake_val)
    curr_cap = 0
    while curr_cap <= capacity:
        for cake in cakes:
            if cake[0] <= curr_cap:
                max_val_at_cap[curr_cap] = max((cake[1] + max_val_at_cap[curr_cap - cake[0]]), max_val_at_cap[curr_cap])
        curr_cap += 1
    return max_val_at_cap[capacity]


def main():
    assert max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20) == 555
    pass


if __name__ == '__main__':
    main()
