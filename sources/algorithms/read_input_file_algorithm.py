class InvalidInputError(Exception):
    """Exception raised for invalid input."""
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)

def read_input_file(filename):
    """Reads the input file and returns number of floors, lift capacity, and requests as a 2D array."""
    # initialise variables
    num_floors = 0
    lift_capacity = 0
    requests = []

    with open(filename, 'r') as file:
            lines = file.readlines()

            # read number of floors and lift capacity
            for line in lines:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                if "," in line:
                    try:
                        parts = line.split(",")
                        # presence check for num_floors and capacity
                        if len(parts) != 2 or not parts[0].strip():  
                            raise InvalidInputError("Invalid input provided. Line 2 in inputFile.")
                        num_floors, lift_capacity = map(int, line.split(","))
                    # ensures both are integers
                    except(ValueError): 
                        raise InvalidInputError(message="Invalid input provided. Line 2 in input file, non-integer value.")
                    # initialize a 2D array
                    requests = [[] for _ in range(num_floors)]  
                    break

            # read floor requests
            for line in lines:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                if ":" in line:
                    floor, destinations = line.split(":")
                    # convert floor to 0-based index
                    floor = int(floor.strip()) - 1  
                    if destinations.strip():
                        requests[floor] = list(map(int, destinations.split(",")))
    return num_floors, lift_capacity, requests