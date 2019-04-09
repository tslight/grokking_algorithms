def main():
    arr = input("Enter a series of numbers separated by spaces: ")
    arr = arr.split()
    arr = [int(e) for e in arr]
    print("Original array: {}".format(arr))
    sorted_arr = selection_sort(arr)
    print("Sorted array: {}".format(sorted_arr))


if __name__ == '__main__':
    main()
