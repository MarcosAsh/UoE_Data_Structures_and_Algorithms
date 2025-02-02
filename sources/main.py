import tkinter as tk
import time
import threading
from Components.lift import lift
from Components.building import building
from Components.floor import Floor
from Components.person import Person
from algorithms.scan_algorithm import scan_algorithm_real_time

class LiftSimulation:
    def __init__(self, root, num_floors=10, lift_capacity=5):
        self.root = root
        self.num_floors = num_floors
        self.lift_capacity = lift_capacity
        self.current_floor = 0
        self.people_waiting = {i: [] for i in range(num_floors)}  # People waiting per floor
        self.people_in_lift = []
        
        self.canvas = tk.Canvas(root, width=400, height=500, bg="white")
        self.canvas.pack()
        
        self.draw_building()
        self.lift_rect = self.canvas.create_rectangle(150, 450, 250, 500, fill="gray")
        
        self.start_simulation()

    def draw_building(self):
        """Draw floors and labels"""
        for i in range(self.num_floors):
            y = 450 - (i * 50)
            self.canvas.create_line(50, y, 350, y, fill="black")
            self.canvas.create_text(30, y + 20, text=f"Floor {i}", font=("Arial", 12))
    
    def update_lift_position(self, new_floor):
        """Move lift up or down"""
        y_offset = (self.current_floor - new_floor) * 50
        self.canvas.move(self.lift_rect, 0, y_offset)
        self.current_floor = new_floor
        self.root.update()

    def simulate_people_movement(self, target_floor):
        """Animate people entering/exiting the lift"""
        self.canvas.delete("people")
        
        # People leaving the lift
        self.people_in_lift = [p for p in self.people_in_lift if p != target_floor]
        
        # People entering the lift
        if target_floor in self.people_waiting:
            while len(self.people_in_lift) < self.lift_capacity and self.people_waiting[target_floor]:
                self.people_in_lift.append(self.people_waiting[target_floor].pop(0))
        
        # Draw people in lift
        for idx, _ in enumerate(self.people_in_lift):
            self.canvas.create_oval(180 + idx * 10, 460 - (self.current_floor * 50), 
                                    190 + idx * 10, 470 - (self.current_floor * 50), 
                                    fill="blue", tags="people")

        self.root.update()

    def start_simulation(self):
        """Run the lift using SCAN algorithm"""
        requests = [2, 5, 8, 3, 7]  # Sample requests
        my_lift = lift(current_floor=0, doors_open=False, moving=False, direction=1, capacity=self.lift_capacity)

        # Add people to waiting list
        for req in requests:
            self.people_waiting[0].append(req)

        def run_lift():
            total_seek, seek_sequence = scan_algorithm_real_time(requests, my_lift.current_floor, my_lift.direction, self.num_floors)

            for floor in seek_sequence:
                time.sleep(1)
                self.update_lift_position(floor)
                self.simulate_people_movement(floor)

        threading.Thread(target=run_lift, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lift Simulation")
    app = LiftSimulation(root)
    root.mainloop()
