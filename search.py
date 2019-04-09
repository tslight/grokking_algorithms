from argparse import ArgumentParser
import sys
import timeit


def get_args():
    parser = ArgumentParser(description='Binary search')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--binary', action='store_true',
                       help="Run a binary search.")
    group.add_argument('-r', '--recursive', action='store_true',
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


def simple(mylist, item):
    count = 0
    for e in mylist:
        count += 1
        if e == item:
            return (True, count)
    return (False, count)


def binary(mylist, item):
    low = 0
    count = 0
    high = len(mylist) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = mylist[mid]
        count += 1
        if guess == item:
            return (True, count)
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return (False, count)


def recursive_binary(arr, element, count):
    count += 1
    low = 0
    high = len(arr) - 1
    mid = int((low + high) / 2)
    if element == arr[mid]:
        return (True, count)
    elif high == 0:
        return (False, count)
    elif element > arr[mid]:
        return recursive_binary(arr[mid + 1:], element, count)
    elif element < arr[mid]:
        return recursive_binary(arr[:mid - 1], element, count)


def search():
    args = get_args()
    mylist = list(range(0, args.max, args.step))

    if args.binary:
        found, count = binary(mylist, args.number)
        search_type = "binary"
    elif args.recursive:
        found, count = recursive_binary(mylist, args.number, 0)
        search_type = "recursive binary"
    else:
        found, count = simple(mylist, args.number)
        search_type = "simple"

    if found:
        print("Found {} in {} steps, using {} search.".format(
            args.number, count, search_type
        ))
    else:
        print("{} not found in array in {} steps, using {} search.".format(
            args.number, count, search_type
        ))


def main():
    speed = timeit.timeit(
        "search()", setup="from __main__ import search", number=1
    )
    print("Search took {} seconds".format(speed))


if __name__ == '__main__':
    main()
