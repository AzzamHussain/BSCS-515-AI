def dfs(graph, start):
    visited = set()  # To keep track of visited nodes
    stack = [start]  # Initialize the stack with the starting node

    while stack:
        node = stack.pop()  # Pop the top node from the stack
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Process the node (print its value, for example)
            # Push all unvisited neighbors onto the stack
            for neighbor in reversed(graph[node]):  
                if neighbor not in visited:
                    stack.append(neighbor)

# Example :
graph = {
    'A':['B','C','D'],
    'B':['E'], 
    'C':['D','E'], 
    'D':[], 
    'E':[]
}

dfs(graph, 'A')  # Start DFS from node A