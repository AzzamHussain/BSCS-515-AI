import tkinter as tk  # Import the tkinter library for GUI
from tkinter import ttk, messagebox  # Import specific modules from tkinter
from queue import Queue  # Import the Queue class
import heapq  # Import heapq module for priority queue implementation
from collections import deque  # Import deque from collections module
import random  # Import random module for random exploration

class UniformedSearchGUI:
    def __init__(self, master):
        # Initialize the GUI
        self.master = master
        self.master.title("Uniformed Search Strategies")  # Set the title of the GUI window
        self.graph = {}  # Initialize an empty dictionary for storing graph information

        self.canvas = tk.Canvas(self.master, width=400, height=50)  # Create a canvas widget
        self.canvas.pack()  # Pack the canvas widget into the GUI window

        self.create_widgets()  # Call the function to create GUI widgets

    def create_widgets(self):
        # Create nodes entry and label
        self.lbl_nodes = ttk.Label(self.master, text="Nodes (comma-separated):")  # Create a label widget
        self.lbl_nodes.pack()  # Pack the label widget into the GUI window

        self.nodes_entry = ttk.Entry(self.master)  # Create an entry widget for nodes
        self.nodes_entry.pack()  # Pack the entry widget into the GUI window

        # Create edges entry and label
        self.lbl_edges = ttk.Label(self.master, text="Edges (comma-separated, from-to-cost):")  # Create a label widget
        self.lbl_edges.pack()  # Pack the label widget into the GUI window

        self.edges_entry = ttk.Entry(self.master)  # Create an entry widget for edges
        self.edges_entry.pack()  # Pack the entry widget into the GUI window

        # Create start node entry and label
        self.lbl_start_node = ttk.Label(self.master, text="Start Node:")  # Create a label widget
        self.lbl_start_node.pack()  # Pack the label widget into the GUI window

        self.start_node_entry = ttk.Entry(self.master)  # Create an entry widget for start node
        self.start_node_entry.pack()  # Pack the entry widget into the GUI window

        # Create goal node entry and label
        self.lbl_goal_node = ttk.Label(self.master, text="Goal Node:")  # Create a label widget
        self.lbl_goal_node.pack()  # Pack the label widget into the GUI window

        self.goal_node_entry = ttk.Entry(self.master)  # Create an entry widget for goal node
        self.goal_node_entry.pack()  # Pack the entry widget into the GUI window

        # Create maximum steps entry and label
        self.lbl_max_steps = ttk.Label(self.master, text="Maximum Steps:")  # Create a label widget
        self.lbl_max_steps.pack()  # Pack the label widget into the GUI window

        self.max_steps_entry = ttk.Entry(self.master)  # Create an entry widget for maximum steps
        self.max_steps_entry.pack()  # Pack the entry widget into the GUI window

        # Frame for search algorithm buttons
        self.search_algo_frame = ttk.Frame(self.master)  # Create a frame widget
        self.search_algo_frame.pack(side=tk.TOP, padx=10, pady=10)  # Pack the frame widget into the GUI window

        # Buttons for various search algorithms
        self.btn_bfs = ttk.Button(self.search_algo_frame, text="Breadth-First Search (BFS)", command=self.breadth_first_search)  # Create a button widget
        self.btn_bfs.pack(side=tk.LEFT, padx=5, pady=5)  # Pack the button widget into the frame

        self.btn_ucs = ttk.Button(self.search_algo_frame, text="Uniform Cost Search (UCS)", command=self.uniform_cost_search)  # Create a button widget
        self.btn_ucs.pack(side=tk.LEFT, padx=5, pady=5)  # Pack the button widget into the frame

        self.btn_dfs = ttk.Button(self.search_algo_frame, text="Depth-First Search (DFS)", command=self.depth_first_search)  # Create a button widget
        self.btn_dfs.pack(side=tk.LEFT, padx=5, pady=5)  # Pack the button widget into the frame

        self.btn_iddfs = ttk.Button(self.search_algo_frame, text="Iterative Deepening DFS (IDDFS)", command=self.iterative_deepening_dfs)  # Create a button widget
        self.btn_iddfs.pack(side=tk.LEFT, padx=5, pady=5)  # Pack the button widget into the frame

        self.btn_random = ttk.Button(self.search_algo_frame, text="Random Explore", command=self.random_explore)  # Create a button widget
        self.btn_random.pack(side=tk.LEFT, padx=5, pady=5)  # Pack the button widget into the frame

        # Configure frames appearance
        self.configure_frames()  # Call the function to configure frame appearance

    def configure_frames(self):
        # Configure search algorithm frame appearance
        self.search_algo_frame.configure(relief=tk.RIDGE, borderwidth=2, style="SearchAlgo.TFrame")  # Configure the frame

        # Define a custom style for the frame
        self.master.style = ttk.Style()  # Create a style object
        self.master.style.configure("SearchAlgo.TFrame", background="light grey", padx=10, pady=10)  # Configure the style

    def create_graph(self):
        nodes = self.nodes_entry.get().split(',')  # Get nodes input and split by comma
        edges = self.edges_entry.get().split(',')  # Get edges input and split by comma

        for node in nodes:  # Iterate over nodes
            self.graph[node.strip()] = {}  # Add node to graph dictionary

        for edge in edges:  # Iterate over edges
            from_node, to_node, cost = edge.strip().split('-')  # Split edge by '-'
            self.graph[from_node][to_node] = int(cost)  # Add edge to graph dictionary
            self.graph[to_node][from_node] = int(cost)  # Add edge to graph dictionary

    def breadth_first_search(self):
        # Breadth-First Search (BFS) algorithm
        self.create_graph()  # Call function to create graph
        start_node = self.start_node_entry.get()  # Get start node from input
        goal_node = self.goal_node_entry.get()  # Get goal node from input
        path = self.bfs(start_node, goal_node)  # Call BFS function
        self.show_result("BFS Result", start_node, goal_node, path)  # Show result in message box

    def bfs(self, start, goal):
        # Breadth-First Search (BFS) algorithm implementation
        visited = set()  # Initialize set to store visited nodes
        queue = deque([(start, [])])  # Initialize deque for BFS queue

        while queue:  # Loop until queue is empty
            current, path = queue.popleft()  # Dequeue a node from the queue
            if current == goal:  # Check if current node is the goal node
                return path + [current]  # Return   the path to the goal node
            if current not in visited:  # Check if current node is not visited
                visited.add(current)  # Mark current node as visited
                for neighbor, _ in self.graph.get(current, {}).items():  # Iterate over neighbors of current node
                    if neighbor not in visited:  # Check if neighbor is not visited
                        queue.append((neighbor, path + [current]))  # Enqueue neighbor node

        return None  # Return None if no path found

    def uniform_cost_search(self):
        # Uniform Cost Search (UCS) algorithm
        self.create_graph()  # Call function to create graph
        start_node = self.start_node_entry.get()  # Get start node from input
        goal_node = self.goal_node_entry.get()  # Get goal node from input
        path = self.ucs(start_node, goal_node)  # Call UCS function
        self.show_result("UCS Result", start_node, goal_node, path)  # Show result in message box

    def ucs(self, start, goal):
        # Uniform Cost Search (UCS) algorithm implementation
        visited = set()  # Initialize set to store visited nodes
        priority_queue = [(0, start, [])]  # Initialize priority queue for UCS

        while priority_queue:  # Loop until priority queue is empty
            cost, current, path = heapq.heappop(priority_queue)  # Pop node with lowest cost from priority queue
            if current == goal:  # Check if current node is the goal node
                return path + [(current, cost)]  # Return the path to the goal node
            if current not in visited:  # Check if current node is not visited
                visited.add(current)  # Mark current node as visited
                for neighbor, edge_cost in self.graph.get(current, {}).items():  # Iterate over neighbors of current node
                    if neighbor not in visited:  # Check if neighbor is not visited
                        heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [(current, cost)]))  # Push neighbor node to priority queue

        return None  # Return None if no path found

    def depth_first_search(self):
        # Depth-First Search (DFS) algorithm
        self.create_graph()  # Call function to create graph
        start_node = self.start_node_entry.get()  # Get start node from input
        goal_node = self.goal_node_entry.get()  # Get goal node from input
        path = self.dfs(start_node, goal_node)  # Call DFS function
        self.show_result("DFS Result", start_node, goal_node, path)  # Show result in message box

    def dfs(self, start, goal):
        # Depth-First Search (DFS) algorithm implementation
        visited = set()  # Initialize set to store visited nodes
        stack = [(start, [])]  # Initialize stack for DFS

        while stack:  # Loop until stack is empty
            current, path = stack.pop()  # Pop a node from the stack
            if current == goal:  # Check if current node is the goal node
                return path + [current]  # Return the path to the goal node
            if current not in visited:  # Check if current node is not visited
                visited.add(current)  # Mark current node as visited
                for neighbor, _ in self.graph.get(current, {}).items():  # Iterate over neighbors of current node
                    if neighbor not in visited:  # Check if neighbor is not visited
                        stack.append((neighbor, path + [current]))  # Push neighbor node to stack

        return None  # Return None if no path found

    def iterative_deepening_dfs(self):
        # Iterative Deepening Depth-First Search (IDDFS) algorithm
        self.create_graph()  # Call function to create graph
        start_node = self.start_node_entry.get()  # Get start node from input
        goal_node = self.goal_node_entry.get()  # Get goal node from input
        path = self.iddfs(start_node, goal_node)  # Call IDDFS function
        self.show_result("IDDFS Result", start_node, goal_node, path)  # Show result in message box

    def iddfs(self, start, goal):
        # Iterative Deepening Depth-First Search (IDDFS) algorithm implementation
        depth_limit = 0  # Initialize depth limit
        while True:  # Loop indefinitely
            result = self.dls(start, goal, depth_limit)  # Call DLS function with current depth limit
            if result is not None:  # Check if result is found
                return result  # Return the result
            depth_limit += 1  # Increment depth limit

    def dls(self, node, goal, depth_limit):
        # Depth-Limited Search (DLS) algorithm
        if node == goal:  # Check if current node is the goal node
            return [node]  # Return the goal node
        elif depth_limit == 0:  # Check if depth limit is reached
            return None  # Return None
        elif depth_limit > 0:  # Check if depth limit is not reached
            for neighbor, _ in self.graph.get(node, {}).items():  # Iterate over neighbors of current node
                result = self.dls(neighbor, goal, depth_limit - 1)  # Recursively call DLS with reduced depth limit
                if result is not None:  # Check if result is found
                    return [node] + result  # Return the path to the goal node
            return None  # Return None if no path found

    def random_explore(self):
        # Random Exploration algorithm
        self.create_graph()  # Call function to create graph
        start_node = self.start_node_entry.get()  # Get start node from input
        max_steps = int(self.max_steps_entry.get())  # Get maximum steps from input
        path = self.random_explore_util(start_node, max_steps)  # Call random exploration function
        if path:  # Check if path is not empty
            messagebox.showinfo("Random Exploration Result", f"Random exploration from {start_node} with max steps {max_steps}: {path}")  # Show result in message box
        else:  # If no path found
            messagebox.showwarning("Random Exploration Result", f"No exploration possible from {start_node} within {max_steps} steps")  # Show warning in message box

    def random_explore_util(self, start_node, max_steps):
        # Random Exploration algorithm implementation
        current_node = start_node  # Initialize current node
        steps = 0  # Initialize steps counter
        path = [current_node]  # Initialize path with start node

        while steps < max_steps and current_node != self.goal_node_entry.get():  # Loop until maximum steps reached or goal node found
            neighbors = list(self.graph.get(current_node, {}).keys())  # Get neighbors of current node
            if not neighbors:  # Check if no neighbors
                break  # Break the loop
            current_node = random.choice(neighbors)  # Choose a random neighbor
            path.append(current_node)  # Add chosen neighbor to path
            steps += 1  # Increment steps counter

        return path  # Return the path

    def show_result(self, title, start, goal, path):
        # Function to display search results
        if path:  # Check if path is not empty
            messagebox.showinfo(title, f"Path from {start} to {goal}: {path}")  # Show path in info message box
        else:  # If no path found
            messagebox.showwarning(title, f"No path found from {start} to {goal}")  # Show warning in message box

# Main function to run the GUI
def main():
    root = tk.Tk()  # Create the root window
    app = UniformedSearchGUI(root)  # Create an instance of the GUI class
    root.mainloop()  # Enter the tkinter event loop

if __name__ == "__main__":
    main()  # Call the main function to start the GUI application