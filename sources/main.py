import sys
import os
import threading
import time
import tkinter as tk

# Ensure correct module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import elevator algorithms and building components
from algorithms.scan_algorithm import scan_algorithm_loop
from algorithms.look_algorithm import look_algorithm
from algorithms.my_lift_algorithm import my_lift
from algorithms.read_input_file_algorithm import read_input_file
from components.building import building

class LiftSimulationGUI:
    """
    GUI for simulating an elevator system with multiple algorithms.
    """
    def __init__(self, root, building):
        """
        Initializes the GUI and its components.
        :param root: The Tkinter root window.
        :param building: The building object containing floors and lifts.
        """
        self.root = root
        self.building = building
        self.lift = self.building.get_lift()
        self.algorithms = {
            "SCAN": scan_algorithm_loop,  # Using the looped SCAN algorithm
            "LOOK": look_algorithm,
            "MY_LIFT": my_lift
        }
        self.algorithm = "SCAN"  # Default algorithm

        # Set up window properties
        self.root.title("Lift Simulation")
        self.root.geometry("400x700")

        # Create floor labels
        self.floor_labels = []
        for i in range(self.building.get_num_floors()):
            label = tk.Label(root, text=f"Floor {i+1}: 0 waiting", width=20, height=2, bg='white', relief="solid")
            label.pack(side="bottom")
            self.floor_labels.append(label)

        # Display lift status
        self.lift_status = tk.Label(root, text="Lift: 0 people inside", font=("Arial", 12))
        self.lift_status.pack()

        # Start simulation button
        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

        # Algorithm toggle button
        self.toggle_algorithm_button = tk.Button(root, text="Change Algorithm", command=self.toggle_algorithm)
        self.toggle_algorithm_button.pack()

        # Algorithm label
        self.algorithm_label = tk.Label(root, text=f"Current Algorithm: {self.algorithm}")
        self.algorithm_label.pack()

    def update_gui(self):
        """
        Updates the GUI with the current state of floors and the lift.
        """
        for i, label in enumerate(self.floor_labels):
            num_waiting = self.building.get_floor(i).GetNumPeople()
            people_waiting = [str(p) for p in self.building.get_floor(i).GetPeople().return_queue()]  # ✅ Format people correctly
            label.config(text=f"Floor {i+1}: {num_waiting} waiting - {', '.join(people_waiting)}",
                        bg='green' if i == self.lift.get_current_floor() else 'white')

        self.lift_status.config(text=f"Lift: {self.lift.get_num_people()} people inside")
        self.root.update()


    def toggle_algorithm(self):
        """
        Toggles between available elevator algorithms.
        """
        algo_keys = list(self.algorithms.keys())
        current_index = algo_keys.index(self.algorithm)
        self.algorithm = algo_keys[(current_index + 1) % len(algo_keys)]
        self.algorithm_label.config(text=f"Current Algorithm: {self.algorithm}")
        
    def run_algorithm(self):
        """
        Runs the selected algorithm and updates the GUI accordingly.
        """
        selected_algorithm = self.algorithms[self.algorithm]
        try:
            if self.algorithm == "SCAN":
                scan_algorithm_loop(self.building, self.update_gui)

            elif self.algorithm == "MY_LIFT":
                sequence = selected_algorithm("sources/input_files/input0.txt")
                if not sequence:  
                    print(f"Warning: {self.algorithm} returned no sequence.")
                    return

            else:
                sequence = selected_algorithm(self.building)
                if not sequence:
                    print(f"Warning: {self.algorithm} returned no sequence.")
                    return

            for floor in sequence:
                self.lift.change_current_floor(floor)

                people_to_remove = []
                for person in self.lift.peopleList[:]:  # Copy list to avoid modifying while iterating
                    if person == floor:
                        people_to_remove.append(person)

                for person in people_to_remove:
                    self.lift.remove_people(person)

                floor_obj = self.building.get_floor(floor)
                while self.lift.get_num_people() < self.lift.get_capacity():
                    person = floor_obj.RemoveFromPeople()
                    if person is None:
                        break  # Stop if no more people are waiting
                    self.lift.add_people(person)

                self.update_gui()
                time.sleep(1)

        except Exception as e:
            print(f"Error running {self.algorithm}: {e}")

    def start_simulation(self):
        """
        Starts the lift simulation in a separate thread.
        """
        threading.Thread(target=self.run_algorithm, daemon=True).start()


if __name__ == "__main__":
    # Read input file and initialize building
    try:
        num_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
        sim_building = building(num_floors, lift_capacity, requests)

        # Start GUI
        root = tk.Tk()
        app = LiftSimulationGUI(root, sim_building)
        root.mainloop()

    except TypeError as e:
        print(f"Error initializing building: {e}")
    except AttributeError as e:
        print(f"Error initializing building: {e}")
