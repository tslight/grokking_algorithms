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

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-b', '--bubble', action='store_true',
                       help="Use bubble sort.")
    group.add_argument('-i', '--insertion', action='store_true',
                       help="Use insertion sort.")
    group.add_argument('-m', '--merge', action='store_true',
                       help="Use merge sort.")
    group.add_argument('-p', '--python', action='store_true',
                       help="Use Python's built in sort.")
    group.add_argument('-q', '--quick', action='store_true',
                       help="Use quick sort.")
    group.add_argument('-s', '--selection', action='store_true',
                       help="Use selection sort.")

    parser.add_argument("-c", "--custom", action='append',
                        help="Enter a custom array.")
    parser.add_argument("-M", "--max", type=int, default='1_000_000',
                        help="Maximum number in list.")
    parser.add_argument("-S", "--size", type=int, default='10_000',
                        help="Size of list.")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Print sorted list.")

    return parser.parse_args()


def bubble(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


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

    if args.custom:
        mylist = args.custom
    else:
        mylist = [randint(0, args.max) for i in range(0, args.size)]
        mylist = sorted(mylist, reverse=True)  # make as hard as possible..
    length = len(mylist)

    do_sort = {
        'selection': lambda: selection(mylist),
        'python': lambda: sorted(mylist),
        'quick': lambda: quick(mylist),
        'bubble': lambda: bubble(mylist),
    }
    # arg_kwargs = args._get_kwargs()
    # sort_type = [i[0] for i in arg_kwargs
    #              if i[1] == True and i[0] != 'verbose'][0]
    arg_dict = vars(args)
    sort_type = [key for key, value in arg_dict.items()
                 if value == True and key != 'verbose'][0]
    sorted_arr = do_sort[sort_type]()

    if args.verbose:
        print("\nOriginal array:\n")
        prtcols(mylist)
        print("\nSorted array:\n")
        prtcols(sorted_arr)

    print(
        "\nType: {} Sort".format(sort_type.capitalize()) +
        "\nLength: {:,}".format(length)
    )


def main():
    speed = timeit(
        "mysort()", setup="from __main__ import mysort", number=1
    )
    print("Time: {} seconds\n".format(round(speed, 8)))


if __name__ == '__main__':
    main()
