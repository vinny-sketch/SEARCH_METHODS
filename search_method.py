# =========================================================================
# FOUNDATIONS OF AI (CCS 2226) - PRACTICAL TASK FOUR: SEARCH PATHS
# Student Registration Number: CIT-223-10/2024
#
# Implementation of pathfinding optimization using:
# (i) Breadth-First Search (Layer-by-Layer evaluation via FIFO track)
# (ii) Depth-First Search (Deep-Branch evaluation via LIFO track)
# =========================================================================

from collections import deque

# Custom Network Topography: Swapped out standard alphabetic variables
# for location nodes to represent a simulative routing layout.
NETWORK_MAP = {
    'Station_Alpha': ['Hub_1', 'Hub_2'],
    'Hub_1': ['Sub_A', 'Sub_B'],
    'Hub_2': ['Sub_C', 'Sub_D'],
    'Sub_A': [],
    'Sub_B': ['Target_Terminal'],
    'Sub_C': [],
    'Sub_D': [],
    'Target_Terminal': []
}

# =========================================================================
# (i) BREADTH-FIRST SEARCH OPTIMIZATION (FIFO QUEUE)
# =========================================================================
def compute_bfs_path(routing_grid, initial_state, target_state):
    """
    Explores the closest neighbors systematically layer by layer to 
    determine the shortest structural topological path to the target.
    """
    nodes_processed = set()
    node_queue = deque([(initial_state, [initial_state])])
    nodes_processed.add(initial_state)
    
    while node_queue:
        current_location, tracking_path = node_queue.popleft()
        
        # Check if the node matches the goal state
        if current_location == target_state:
            return tracking_path
            
        # Evaluation of adjacent node paths
        for adjacent_node in routing_grid.get(current_location, []):
            if adjacent_node not in nodes_processed:
                nodes_processed.add(adjacent_node)
                node_queue.append((adjacent_node, tracking_path + [adjacent_node]))
                
    return None

# =========================================================================
# (ii) DEPTH-FIRST SEARCH OPTIMIZATION (LIFO STACK)
# =========================================================================
def compute_dfs_path(routing_grid, initial_state, target_state):
    """
    Traces a single structural branch down to its deepest terminal point 
    before backtracking to evaluate alternate branch possibilities.
    """
    nodes_processed = set()
    node_stack = [(initial_state, [initial_state])]
    
    while node_stack:
        current_location, tracking_path = node_stack.pop()
        
        # Check if the node matches the goal state
        if current_location == target_state:
            return tracking_path
            
        if current_location not in nodes_processed:
            nodes_processed.add(current_location)
            
            # Reverse keeps scanning sequence moving consistently left-to-right
            for adjacent_node in reversed(routing_grid.get(current_location, [])):
                if adjacent_node not in nodes_processed:
                    node_stack.append((adjacent_node, tracking_path + [adjacent_node]))
                    
    return None


# =========================================================================
# SYSTEM EXECUTION INTERFACE
# =========================================================================
if __name__ == "__main__":
    START_POINT = 'Station_Alpha'
    END_POINT = 'Target_Terminal'
    
    print("=================================================================")
    print(f"Analyzing Optimized Search Routes: {START_POINT} -> {END_POINT}")
    print("=================================================================\n")
    
    # 1. Execute Breadth-First Strategy
    calculated_bfs = compute_bfs_path(NETWORK_MAP, START_POINT, END_POINT)
    print("Resulting (i) Breadth-First Search (BFS) Traversal Path:")
    if calculated_bfs:
        print("    --> Path Sequence: " + " -> ".join(calculated_bfs))
    else:
        print("    --> Path query could not resolve destination state.")
        
    print("\n-----------------------------------------------------------------\n")
    
    # 2. Execute Depth-First Strategy
    calculated_dfs = compute_dfs_path(NETWORK_MAP, START_POINT, END_POINT)
    print("Resulting (ii) Depth-First Search (DFS) Traversal Path:")
    if calculated_dfs:
        print("    --> Path Sequence: " + " -> ".join(calculated_dfs))
    else:
        print("    --> Path query could not resolve destination state.")
    print("\n=================================================================")
