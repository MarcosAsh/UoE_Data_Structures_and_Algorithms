def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def scan_algorithm(requests, head, direction, max_floor):
    """
    requests: List of requested floors.
    head: Current floor of the lift.
    direction: Initial direction of movement ('-1' for down or '1' for up).
    max_floor: The highest floor in the building.
    return: Tuple containing the total seek operations and the sequence of visited floors.
    """
    seek_count = 0
    left = []
    right = []
    seek_sequence = []

    if direction == -1:
        left.append(0)
    elif direction == 1:
        right.append(max_floor)

    for req in requests:
        if req < head:
            left.append(req)
        elif req > head:
            right.append(req)

    left = quicksort(left)
    right = quicksort(right)

    run = 2
    while run > 0:
        if direction == -1:
            for i in reversed(left):
                seek_sequence.append(i)
                seek_count += abs(head - i)
                head = i
            direction = 1
        elif direction == 1:
            for i in right:
                seek_sequence.append(i)
                seek_count += abs(head - i)
                head = i
            direction = -1
        run -= 1

    return seek_count, seek_sequence

# Example usage:
requests = [176, 79, 34, 60, 92, 11, 41, 114]
head = 50
direction = -1
max_floor = 200

total_seek, sequence = scan_algorithm(requests, head, direction, max_floor)
print(f"Total seek operations: {total_seek}")
print("Seek sequence:", sequence)
