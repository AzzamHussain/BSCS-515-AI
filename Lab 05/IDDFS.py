def iddfs(graph, start, goal):
    depth_limit = 0  # Start with a depth limit of 0
    print("Start node:", start)  # Print the start node
    while True:  # Repeat until a solution is found or all depths are explored
        result = dls(graph, start, goal, depth_limit)  # Perform Depth-Limited Search (DLS)
        if result is not None:  # If a solution is found, return it
            return result
        depth_limit += 1  # Increment the depth limit for the next iteration

def dls(graph, node, goal, depth_limit):
    return recursive_dls(graph, node, goal, depth_limit)  # Perform Recursive Depth-Limited Search (RDLS)

def recursive_dls(graph, node, goal, depth_limit):
    if node == goal:  # If the current node is the goal, return it
        return node
    elif depth_limit == 0:  # If the depth limit is reached, stop
        return None
    elif depth_limit > 0:  # If the depth limit is not reached yet
        print("Visiting node:", node)  # Print the current node being visited
        for neighbor in graph[node]:  # Explore each neighbor of the current node
            result = recursive_dls(graph, neighbor, goal, depth_limit - 1)  # Recursively perform RDLS
            if result is not None:  # If a solution is found in the subtree, return it
                return result
        return None  # If no solution is found in the subtree, return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
start_node = 'A'
goal_node = 'F'
result = iddfs(graph, start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", result)