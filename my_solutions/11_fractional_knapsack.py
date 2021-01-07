# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """
    Input:
    3 50   => number of items/ capacity of bag
    60 20  => value/weight of item
    100 50 => value/weight of item
    120 30 => value/weight of item

    Output:
    180.0000
    max number of fractions in bag
    in this case we take 1st and 3rd item cause it is the max(value/weight)
    """

    index = list(range(len(values)))
    # print(index)
    # Get fractions values/weights
    fractions = [v / w for v, w in zip(values, weights)]
    # print(fractions)
    # Sort index of fractions by reversal order
    index.sort(key=lambda i: fractions[i], reverse=True)

    max_value = 0
    # fractions => [0,0,0]
    fractions = [0] * len(values)

    for i in index:
        if weights[i] <= capacity:
            # if capacity is larger than weights[i] => take whole of weight and set its' fraction to 1
            fractions[i] = 1
            max_value += values[i]
            capacity -= weights[i]
        else:
            # if not => take part of fraction to be used
            fractions[i] = capacity / weights[i]
            max_value += values[i] * capacity / weights[i]
            break

    # return result

    print(max_value)


get_optimal_value(50, weights=[20, 50, 30], values=[60, 100, 120])

# if __name__ == "__main__":
#     data = list(map(int, sys.stdin.read().split()))
#     n, capacity = data[0:2]
#     values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))
