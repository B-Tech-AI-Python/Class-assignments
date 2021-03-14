from itertools import product
from collections import namedtuple
try:
    from itertools import izip
except ImportError:
    izip = zip


Reward = namedtuple('Reward', 'name value weight volume')

# bagpack, items, weight, volume
bagpack = Reward('bagpack', 0, 25.0, 0.25)

# item, quantity, weight, volumne
items = [Reward('laptop', 3000, 0.3, 0.025),
         Reward('printer', 1800, 0.2, 0.015),
         Reward('headphone', 2500, 2.0, 0.002)]


def tot_value(items_count):
    """
    Given the count of each item in the sack return -1 if they can't be carried or their total value.

    (also return the negative of the weight and the volume so taking the max of a series of return
    values will minimise the weight if values tie, and minimise the volume if values and weights tie).
    """
    global items, bagpack
    weight = sum(n * item.weight for n, item in izip(items_count, items))
    volume = sum(n * item.volume for n, item in izip(items_count, items))
    if weight <= bagpack.weight and volume <= bagpack.volume:
        return sum(n * item.value for n, item in izip(items_count, items)), -weight, -volume
    else:
        return -1, 0, 0


def knapsack():
    global items, bagpack
    # find max of any one item
    max1 = [min(int(bagpack.weight // item.weight),
                int(bagpack.volume // item.volume)) for item in items]

    # Try all combinations of reward items from 0 up to max1
    return max(product(*[range(n + 1) for n in max1]), key=tot_value)


max_items = knapsack()
maxvalue, max_weight, max_volume = tot_value(max_items)
max_weight = -max_weight
max_volume = -max_volume

print("The maximum value achievable (by exhaustive search) is %g." % maxvalue)
item_names = ", ".join(item.name for item in items)
print("\nThe number of %s items to achieve this is: %s" %
      (item_names, max_items))
print("\nThe weight to carry is %.3g, and the volume used is %.3g." %
      (max_weight, max_volume))


def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))


# Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
