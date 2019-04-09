from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser(description='Binary search')
    parser.add_argument("-m", "--max", type=int, required=True,
                        help="Max number in range.")
    parser.add_argument("-s", "--step", type=int, required=True,
                        help="Steps in range.")
    parser.add_argument("-n", "--number", type=int, required=True,
                        help="Number to search for in range.")
    return parser.parse_args()


def binary_search(arr, element, count):
    count += 1
    low = 0
    high = len(arr) - 1
    mid = int((low + high) / 2)
    if element == arr[mid]:
        return (True, count)
    elif high == 0:
        return (False, count)
    elif element > arr[mid]:
        return binary_search(arr[mid + 1:], element, count)
    elif element < arr[mid]:
        return binary_search(arr[:mid - 1], element, count)


def main():
    args = get_args()
    mylist = list(range(0, args.max, args.step))
    found, count = binary_search(mylist, args.number, 0)
    if found:
        print("Found {} in {} steps.".format(args.number, count))
    else:
        print("{} not found in array in {} steps.".format(args.number, count))


if __name__ == '__main__':
    main()
