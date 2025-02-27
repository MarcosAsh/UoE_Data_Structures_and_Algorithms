import time, sys, os
import matplotlib
import matplotlib.pyplot as plt




sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




from algorithms.scan_algorithm import scan_algorithm
from algorithms.look_algorithm import look_algorithm
from algorithms.read_input_file_algorithm import read_input_file
from components.building import building


def measure_time_complexity():
   scan_times = []
   look_times = []
   num_requests = []
  
   for i in range(1, 300):  # Simulating 100 input files
       filename = f"sources/input_files/input{i}.txt"
       num_floors, lift_capacity, requests = read_input_file(filename)
       test_building = building(num_floors, lift_capacity, requests)
      
       # Measure SCAN algorithm time
       start = time.time()
       scan_algorithm(requests, 0, 1, num_floors)
       scan_times.append(time.time() - start)
       """
       # Measure LOOK algorithm time
       start = time.time()
       look_algorithm(test_building)
       look_times.append(time.time() - start)
       """
       num_requests.append(sum(len(floor) for floor in requests))
  
   # Plot results
   plt.figure(figsize=(10, 5))
   plt.scatter(num_requests, scan_times, label='SCAN Algorithm', marker='o')
   # plt.scatter(num_requests, look_times, label='LOOK Algorithm', marker='s')
   plt.xlabel('Number of Requests')
   plt.ylabel('Execution Time (s)')
   plt.title('Time Complexity of SCAN vs LOOK Algorithm')
   plt.legend()
   plt.grid()
   plt.show()


# Run the timing test
if __name__ == "__main__":
   measure_time_complexity()