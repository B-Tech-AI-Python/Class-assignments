# Import the necessary libraries
from itertools import product
from collections import namedtuple
try:
    from itertools import izip
except ImportError:
    izip = zip


def tot_value(items_count):
    """Find total value of items.

    Taking the negative of the weight and the volume so taking the max
    of a series of return values will minimise the weight if values tie,
    and minimise the volume if values and weights tie.

    Args:
        item_count: count of items in knapsack.

    Returns:
        max value of items, weight, volume.
    """
    global items, bagpack
    weight = sum(n * item.weight for n, item in izip(items_count, items))
    volume = sum(n * item.volume for n, item in izip(items_count, items))
    if weight <= bagpack.weight and volume <= bagpack.volume:
        return sum(n * item.value for n, item in izip(items_count, items)), -weight, -volume
    else:
        return -1, 0, 0


def knapsack():
    """Find optimal value.

    Find the max item count for the given items with the
    given knapsack bag weight and volume.

    Returns:
        max items.
    """
    global items, bagpack
    # find max of any one item
    max1 = [max(int(bagpack.weight // item.weight),
                int(bagpack.volume // item.volume)) for item in items]

    # Try all combinations of reward items from 0 up to max1
    return max(product(*[range(n + 1) for n in max1]), key=tot_value)


Reward = namedtuple('Reward', 'name value weight volume')

bagpack = Reward('bagpack', 0, 25.0, 0.25)

items = [Reward('laptop', 3000, 0.3, 0.025),
         Reward('printer', 1800, 0.2, 0.015),
         Reward('headphones', 2500, 2.0, 0.002)]

max_items = knapsack()
maxvalue, max_weight, max_volume = tot_value(max_items)
max_weight = -max_weight
max_volume = -max_volume

print("The maximum value achievable (by brute force/exhaustive search) is %g." % maxvalue)
item_names = ", ".join(item.name for item in items)
print("\nThe number of %s items to achieve this is: %s" %
      (item_names, max_items))
print("\nThe weight to carry is %.3g, and the volume used is %.3g." %
      (max_weight, max_volume))
