import random

def random_explore(graph, start_node, max_steps):
    current_node = start_node
    steps = 0

    while steps < max_steps:
        print(current_node, end=" ")  # Process the current node
        neighbors = graph.get(current_node, [])  # Get neighbors of the current node
        if not neighbors:
            break  # No neighbors, so stop exploring
        current_node = random.choice(neighbors)  # Move to a random neighbor
        steps += 1

# Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }

random_explore(graph, 'A', max_steps=5)  # Start exploring from node 'A', with maximum 5 steps