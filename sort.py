from argparse import ArgumentParser
from random import randint
from timeit import timeit
from columns import prtcols


def get_args():
    parser = ArgumentParser(
        description='Sort a list using a variety of algorithms. ' +
        'Defaults to creating a list of 10 thousand elements, randomly, ' +
        'from a pool of integers between 0 and 1 million and sorting them ' +
        'with a custom quick sort algorithm.'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--selection', action='store_true',
                       help="Use selection sort.")
    group.add_argument('-q', '--quick', action='store_true',
                       help="Use quick sort.")
    group.add_argument('-p', '--python', action='store_true',
                       help="Use Python's built in sort.")
    parser.add_argument("-m", "--max", type=int, default='1_000_000',
                        help="Maximum number in list.")
    parser.add_argument("-S", "--size", type=int, default='10_000',
                        help="Size of list.")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Print sorted list.")
    return parser.parse_args()


def quick(arr):
    if len(arr) < 2:
        return arr
    else:
        index = int(len(arr) / 2)  # mid point is faster than random element
        # index = randint(0, len(arr) - 1)  # slower than mid point of array
        pivot = arr[index]
        less = [i for i in arr[index + 1:] if i <= pivot]
        greater = [i for i in arr[:index] if i > pivot]
        return quick(less) + [pivot] + quick(greater)


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def mysort():
    args = get_args()
    mylist = [randint(0, args.max) for i in range(0, args.size)]
    mylist = sorted(mylist, reverse=True)  # make as hard as possible..
    length = len(mylist)

    if args.selection:
        sorted_arr = selection(mylist)
        sort_type = "Selection Sort"
    elif args.python:
        sorted_arr = sorted(mylist)
        sort_type = "Python Sort"
    else:
        sorted_arr = quick(mylist)
        sort_type = "Quick Sort"

    if args.verbose:
        print("\nOriginal array:\n")
        prtcols(mylist)
        print("\nSorted array:\n")
        prtcols(sorted_arr)

    print(
        "\nType: {}".format(sort_type) +
        "\nLength: {:,}".format(length)
    )


def main():
    speed = timeit(
        "mysort()", setup="from __main__ import mysort", number=1
    )
    print("Time: {} seconds\n".format(round(speed, 8)))


if __name__ == '__main__':
    main()
