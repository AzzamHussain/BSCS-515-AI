from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue the front node from the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Process the node (print its value, for example)
            # Enqueue all unvisited neighbors of the dequeued node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')  # Start BFS from node A