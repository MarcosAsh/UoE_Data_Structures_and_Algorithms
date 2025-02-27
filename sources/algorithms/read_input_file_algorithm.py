def read_input_file(filename):
    num_floors = 0
    lift_capacity = 0
    requests = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "," in line:
                num_floors, lift_capacity = map(int, line.split(","))
                requests = [[] for _ in range(num_floors)]
                break

        for line in lines:
            line = line.strip()

            if line.startswith("#") or not line:
                continue
            if ":" in line:
                floor, destinations = line.split(":")
                floor = int(floor.strip()) - 1
                if destinations.strip():
                    requests[floor] = list(map(int, destinations.split(",")))
                    
    return num_floors, lift_capacity, requests