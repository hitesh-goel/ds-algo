# Knapsack Problem
# https://www.interviewcake.com/question/python3/cake-thief

def max_duffel_bag_value(cake_tuples, weight_capacity):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        # Set a variable to hold the max monetary value so far for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the current weight
            if cake_weight <= current_capacity:

                # So we check: should we use the cake or not?
                # get the value of current cake + max value of the remaining capacity of duffle bag
                max_value_using_cake = (cake_value + max_values_at_capacities[current_capacity - cake_weight])

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

        # Add each capacity's max value to our list so we can use them when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]

def main():
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity    = 20

    # Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
    max_duffel_bag_value(cake_tuples, capacity)

if __name__ == '__main__':
    main()
