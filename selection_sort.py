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


arr = input("Enter a series of numbers separated by spaces: ")
arr = arr.split()
arr = [int(e) for e in arr]
print("Original array: {}".format(arr))
sorted_arr = selection_sort(arr)
print("Sorted array: {}".format(sorted_arr))
