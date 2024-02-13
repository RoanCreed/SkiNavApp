import heapq as heap
from itertools import permutations

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


def GetAllPermutations(nodes):
    allPermutations = list(permutations(nodes))
    return allPermutations

if __name__ == "__main__":
    # Example graph representation
    graph = {
        'A': {'B': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 4, 'difficulty': 'easy'}},
        'B': {'A': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 5, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
        'C': {'A': {'length': 4, 'difficulty': 'easy'}, 'B': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 1, 'difficulty': 'easy'}},
        'D': {'B': {'length': 5, 'difficulty': 'easy'}, 'C': {'length': 1, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
        'E': {'D': {'length': 2, 'difficulty': 'easy'}}
    }
    
    #Heuristic function, for future
    def Heuristic(node1, node2):
        return 0  
    
    
    
    #start_node = 'A'
    #end_node = 'E'
    
    nodes = ['A', 'B', 'E', 'D']
    allPermutations = GetAllPermutations(nodes)

    shortestPathList = []

    shortestDisPathForEachPermDict = {}
    shortestPathListForEachPermList =[]
    

    for p in allPermutations:
        total_distance = 0
        total_path = []
        #print("--------------New perm_______________")
        #print("-----",p,"------")
        
        for i in range(len(p) - 1):
            pair = (p[i], p[i + 1])
            #print(pair)

            shortestDistancePathForCurrentPermutationDict = {}

            start_node, end_node = pair

            shortestPathForCurrentPermutation = AStar(graph, start_node, end_node, Heuristic)
            if shortestPathForCurrentPermutation is not None:
                distance = CalculateTotalDistance(shortestPathForCurrentPermutation, graph)

                shortestDistancePathForCurrentPermutationDict = {'distance': distance, 'path': shortestPathForCurrentPermutation}
                shortestPathList.append(shortestDistancePathForCurrentPermutationDict)

                total_distance += distance
                total_path.append(shortestPathForCurrentPermutation)

                #print(distance,shortestPathForCurrentPermutation)



    
        # Construct the dictionary
        shortestDisPathForEachPermDict = {'distance': total_distance, 'path': total_path} #this not the path but the permutation, the path must concatinate all the paths from each pair
        shortestPathListForEachPermList.append(shortestDisPathForEachPermDict)

        print("Total Distance: ", total_distance, "| Total Path: ", total_path)

    for key, value in shortestDisPathForEachPermDict.items():
        print(key, ":", value)

# Initialize with a large value
min_distance = float('inf')
min_path = None

# Iterate through each dictionary in the list
for shortestDisPathForEachPermDict in shortestPathListForEachPermList:
    # Get distance and path from the current dictionary
    distance = shortestDisPathForEachPermDict['distance']
    path = shortestDisPathForEachPermDict['path']

    # Compare distance with the current minimum distance
    if distance < min_distance:
        min_distance = distance  # Update minimum distance
        min_path = path  # Update path

# Print the smallest distance and corresponding path
print("Smallest distance:", min_distance)
print("Corresponding path:", min_path)