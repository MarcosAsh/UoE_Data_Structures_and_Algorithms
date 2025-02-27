def median_of_three(arr):
    # Gets first, middle, and last element from list
    first, middle, last = arr[0], arr[len(arr) //2], arr[-1]

    # If middle is median return middle value
    if first <= middle <= last or last <= middle <= first:
        return middle
    # If last is median return last
    elif middle <= last <= first or first <= last <= middle:
        return last
    # Else first is median so return first
    else:
        return first

def quicksort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Set pivot point to be middle element
    pivot = median_of_three(arr)

    # Obtain left and right lists, along with middle element based on pivot point
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively call quicksort as divide and conquer finalising by merging arrays
    return quicksort(left) + middle + quicksort(right)