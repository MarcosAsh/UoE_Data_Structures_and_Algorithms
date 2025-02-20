import os, random

# create folder if doesnt exist
folder_name = "sources/input_files"
os.makedirs(folder_name, exist_ok=True)

# make 200 files
for floornum in range(300):
    # make file name sequentially and put into input_files folder
    file_name = os.path.join(folder_name, f"input{floornum}.txt")
    # defines the number of floors and the capacity
    num_floors = random.randint(3, 30)
    capacity = 5

    # creates/overwrites if exists
    with open(file_name, "w") as file:
        # write header
        file.writelines("# Number of Floors, Capacity\n")
        # write total number of floors and lift capacity
        file.writelines(f"{num_floors}, {capacity}\n")
        # write floor header
        file.writelines("# Floor Requests\n")

        # iterates through each floor
        for i in range(num_floors):
            # randomises number of requests
            request_num = random.randint(1, capacity)
            # creates array with all possible floors (excludes the current floor)
            choices = [j for j in range(0, num_floors) if j != floornum]
            requests = []
            # adds as many random floors to requests as requests
            for k in range(request_num):
                # added as strings so can be joined
                requests.append(str(random.choice(choices)))
            requests_str = ", ".join(requests)
            # makes sure last line does not have a new line
            if i >= num_floors - 1:
                file.writelines(f"{i}: {requests_str}")
            else:
                file.writelines(f"{i}: {requests_str}\n")