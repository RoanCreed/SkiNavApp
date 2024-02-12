import heapq as heap


def ReconstructShortestPath(currentNode, predecessors, start):
    path = []
    while currentNode in predecessors:
        path.insert(0, currentNode)
        currentNode = predecessors[currentNode]
    path.insert(0, start)

    return path

def AStar(graph, start, end, Heuristic):
    # Init starting distances (infinite)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    #priority queue - stores nodes with current distances known
    pq = [(Heuristic(start, end), 0, start)]  # Tuple: (total_cost, current_cost, node)

    #Dictionary that stores predecessors of each node
    predecessors = {}

    while pq:
        #Pop the node with the smallest total cost
        total_cost, current_cost, currentNode = heap.heappop(pq)

        #Check if the node is the destination
        if currentNode == end:
            #Recontruct the shortest path
            path = ReconstructShortestPath(currentNode, predecessors, start)

            return path

        #If not then explore neighbours of currentNode
        for neighbouringNode, nodeData in graph[currentNode].items():
            length = nodeData['length']
            difficulty = nodeData['difficulty']

            #Adjust for difficulty
            if difficulty == 'easy':
                length *= 0.5  
            elif difficulty == 'medium':
                length *= 1.0  
            elif difficulty == 'hard':
                length *= 2.0  

            distance = current_cost + length

            if distance < distances[neighbouringNode]:
                distances[neighbouringNode] = distance
                predecessors[neighbouringNode] = currentNode
                heap.heappush(pq, (distance + Heuristic(neighbouringNode, end), distance, neighbouringNode))
            
    #If destination is unreachable
    return None


def CalculateTotalDistance(path, graph):
    totalDistance = 0

    for i in range(len(path) - 1):
        currentNode = path[i]
        nextNode = path[i + 1]

        if nextNode in graph[currentNode]:
            totalDistance += graph[currentNode][nextNode]['length']
        else:
            print(f"No direct edge between {currentNode} and {nextNode}.")
            return None
    
    return totalDistance
#here is a new comment

if __name__ == "__main__":
    # Example graph representation
    graph = {
        'A': {'B': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 4, 'difficulty': 'medium'}},
        'B': {'A': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 2, 'difficulty': 'medium'}, 'D': {'length': 5, 'difficulty': 'hard'}, 'E': {'length': 10, 'difficulty': 'hard'}},
        'C': {'A': {'length': 4, 'difficulty': 'medium'}, 'B': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 1, 'difficulty': 'hard'}},
        'D': {'B': {'length': 5, 'difficulty': 'hard'}, 'C': {'length': 1, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
        'E': {'D': {'length': 2, 'difficulty': 'hard'}}
    }
    
    #Heuristic function, for future
    def Heuristic(node1, node2):
        return 0  
    
    start_node = 'A'
    end_node = 'E'
    
    shortest_path = AStar(graph, start_node, end_node, Heuristic)
    print("Shortest Path:", shortest_path)
    if shortest_path is not None:
        distance = CalculateTotalDistance(shortest_path, graph)
    
        print("Distance:", distance)
