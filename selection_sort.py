from argparse import ArgumentParser


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


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def main():
    arr = input("Enter a series of numbers separated by spaces: ")
    arr = arr.split()
    arr = [int(e) for e in arr]
    print("Original array: {}".format(arr))
    sorted_arr = selection_sort(arr)
    print("Sorted array: {}".format(sorted_arr))


if __name__ == '__main__':
    main()
