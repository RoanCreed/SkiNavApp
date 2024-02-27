import heapq as heap
from itertools import permutations


def Weighter(edge: dict, weights: dict) -> dict: 
    """
    weights of format:
    {
        "lift": float,
        "novice": float,
        "easy": float,
        "intermediate": float,
        "advanced": float
    }
    returns the node weight as float
    """
    weight = weights.get(edge.get("difficulty"))
    if weight is None:
        weight = 1
    weight = edge.get("duration") * edge.get("distance_prop") * weight

    return weight


def ReconstructShortestPath(currentNode, predecessors, start):
    path = []   #To store recontructed path
    while currentNode in predecessors:  #Loop through predecessors dict (back tracking)
        path.insert(0, currentNode) #inserts current node to beginning of path list
        currentNode = predecessors[currentNode] #Move to the next predecessor node
    path.insert(0, start)   #set the start to the initial node

    return path


def AStar(graph, start, end, weights):
    # Init starting distances (infinite)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    #priority queue - stores nodes with current distances known
    pq = [(0, 0, start)]  # Tuple: (total_cost, current_cost, node)

    #Dictionary that stores predecessors of each node
    predecessors = {}

    while pq:
        #Pop the node with the smallest total cost
        total_cost, current_cost, currentNode = heap.heappop(pq)

        #Check if the node is the destination
        if currentNode == end:
            #If so Recontruct the shortest path and return
            path = ReconstructShortestPath(currentNode, predecessors, start)

            return path

        #If not then explore neighbours of currentNode
        for neighbouringNode, nodeData in graph[currentNode].items():
            print(nodeData)
            distance = Weighter(nodeData, weights)

            if distance < distances[neighbouringNode]:  # Check if the distance to the neighbouring node is shorter than the current known distance
                distances[neighbouringNode] = distance  # Update the distance to the neighbouring node
                predecessors[neighbouringNode] = currentNode  # Update the predecessor node of the neighbouring node
                # Push the neighbouring node into the priority queue with updated distance
                heap.heappush(pq, (distance , distance, neighbouringNode))
    
    #If destination is unreachable
    return None


def CalculateTotalDistance(path, graph, weights):
    totalDistance = 0

    # Go through pairs of nodes in the path
    for i in range(len(path) - 1):
        currentNode = path[i]
        nextNode = path[i + 1]

        if nextNode in graph[currentNode]:  #If there is a direct edge
            totalDistance += Weighter(graph[currentNode][nextNode], weights)  #Add the length to the total distance
        else:
            print(f"No direct edge between {currentNode} and {nextNode}.")  #Error if not
            return None
    
    return totalDistance


def GetAllPermutations(nodes):
    allPermutations = list(permutations(nodes))
    return allPermutations