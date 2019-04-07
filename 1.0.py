from argparse import ArgumentParser
import sys
import time


def get_args():
    parser = ArgumentParser(description='Binary search')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--binary', action='store_true',
                       help="Run a binary search.")
    group.add_argument('-s', '--simple', action='store_true',
                       help="Run a simple search.")
    parser.add_argument("-m", "--max", type=int, required=True,
                        help="Max number in range.")
    parser.add_argument("-S", "--step", type=int, required=True,
                        help="Steps in range.")
    parser.add_argument("-n", "--number", type=int, required=True,
                        help="Number to search for in range.")
    return parser.parse_args()


def simple_search(mylist, item):
    count = 0
    for e in mylist:
        count += 1
        if e == item:
            print(
                "Found {} at position {}.\n".format(
                    e,
                    mylist.index(e)
                ) +
                "Search took {} steps.".format(
                    count
                )
            )
            return
    print("Cannot find {} in list.".format(item))


def binary_search(mylist, item):
    low = 0
    count = 0
    high = len(mylist) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = mylist[mid]
        count += 1
        if guess == item:
            print(
                "Found {} at position {}.\n".format(
                    guess,
                    mid
                ) +
                "Search took {} steps.".format(
                    count
                )
            )
            return
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print("Cannot find {} in list.".format(item))


args = get_args()
mylist = list(range(0, args.max, args.step))
start = time.time()
if args.binary:
    binary_search(mylist, args.number)
else:
    simple_search(mylist, args.number)
end = time.time()
time = format(end - start)
print("Search took {}".format(time))
