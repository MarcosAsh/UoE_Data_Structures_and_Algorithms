# look algorithm
def quicksort(arr):
    if len(arr) <= 1:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
def look_algorithm(floors, requests, current_floor, direction):
    while requests:
        requests = quicksort(requests)
        print(f"Current floor: {current_floor}")
        print(f"Requests: {requests}")

        if direction == 1: 
            next_requests = [req for req in requests if req >= current_floor]
            if next_requests:
                next_floor = min(next_requests)
            else:
                direction = -1
                continue
        else:
            next_requests = [req for req in requests if req >= current_floor]
            if next_requests:
                next_floor = max(next_requests)
            else:
                direction = 1
                continue 
        current_floor = next_floor
        requests.remove(current_floor)
    return current_floor

# test code
requests = [0, 5, 3, 7, 9, 2]
floors = 10
final_floor = look_algorithm(floors, requests)
print(f"Final Floor: {final_floor}")