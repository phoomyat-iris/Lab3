print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1

# Sorts fewer than 10 integers; returns 0, 1 or 2 for invalid input (REQ-03 to REQ-05)
def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # REQ-04: no numbers entered
    if n == 0:
        return 0

    # REQ-03: 10 or more numbers entered
    if n >= 10:
        return 1

    # REQ-05: any value is not an integer
    for value in arr_result:
        if not isinstance(value, int):
            return 2

    # Invalid sorting order: return an empty array
    if sorting_order != SORT_ASCENDING and sorting_order != SORT_DESCENDING:
        return []

    # REQ-01 / REQ-02: fewer than 10 integers, sort the list
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result


def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)


if __name__ == "__main__":
    main()
