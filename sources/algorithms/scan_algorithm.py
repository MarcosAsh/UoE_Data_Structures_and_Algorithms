# quick sort for scan algorithm
def quicksort(arr):
    if len(arr) <= 1:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
# scan algorithm

size = 8
desk_size = 200

def scan(arr, head, direction):
    seek_count = 0
    distance, current_track = 0, 0
    left = []
    right = []
    seek_sequence = []

    if direction == 'left':
        left.append(0)
    elif direction == 'right':
        right.append(0)

    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

    # sorting right and left vectors
    quicksort(left)
    quicksort(right)

    run = 2
    while (run != 0):
        if (direction == 'left'):
            for i in range(len(left) - 1, -1, -1):
                current_track = left[i]
                seek_sequence.append(current_track)
                distance = abs(current_track - head)
                seek_count += distance
                head = current_track
            direction = 'right'
        elif (direction == 'right'):
            for i in range(len(right)):
                current_track = right[i]
                seek_sequence.append(current_track)
                distance = abs(current_track - head)
                seek_count += distance
                head = current_track
            direction = 'left'
        run -= 1
    print(f"Total number of seek operations = : {seek_count}")
    print("Seek sequence is : ")
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

# test code
arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
head = 50
direction = "left"

scan(arr, head, direction)