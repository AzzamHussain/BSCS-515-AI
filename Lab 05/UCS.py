import heapq

def ucs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    priority_queue = [(0, start, [])]  # Priority queue: (cumulative cost, current node, path)
    
    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)  # Dequeue the node with the lowest cost
        
        if current in visited:
            continue
        
        visited.add(current)  # Mark the current node as visited
        path = path + [(current, cost)]  # Update the path with the current node and its cost
        
        if current == goal:
            return path  # Return the path if the goal is reached
        
        for neighbor, edge_cost in graph.get(current, {}).items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path.copy()))  # Enqueue the neighbor
    
    return None  # Return None if no path is found

# Example usage:
graph = {
    'A': {'B': 1, 'C': 5},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 3},
    'D': {},
    'E': {'G': 1},
    'F': {},
    'G': {}
}
start_node = 'A'
goal_node = 'G'
result = ucs(graph, start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", result)