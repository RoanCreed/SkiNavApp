import PathFinder


if __name__ == "__main__":

    # graph = {
    #     'A': {'B': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 4, 'difficulty': 'easy'}},
    #     'B': {'A': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 5, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
    #     'C': {'A': {'length': 4, 'difficulty': 'easy'}, 'B': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 1, 'difficulty': 'easy'}},
    #     'D': {'B': {'length': 5, 'difficulty': 'easy'}, 'C': {'length': 1, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
    #     'E': {'D': {'length': 2, 'difficulty': 'easy'}}
    # }


    graph = {
        'A': {'B': {'length': 3, 'difficulty': 'medium'}, 'E': {'length': 3, 'difficulty': 'easy'}, 'F': {'length': 5, 'difficulty': 'medium'}},
        'B': {'C': {'length': 5, 'difficulty': 'medium'}, 'L': {'length': 7, 'difficulty': 'medium'}},
        'C': {'D': {'length': 5, 'difficulty': 'medium'}},
        'D': {'G': {'length': 6, 'difficulty': 'medium'}, 'H': {'length': 7, 'difficulty': 'medium'}},
        'E': {'F': {'length': 6, 'difficulty': 'medium'}, 'W': {'length': 6, 'difficulty': 'easy'}},
        'F': {'D': {'length': 6, 'difficulty': 'medium'}},
        'G': {'H': {'length': 3, 'difficulty': 'medium'}, 'I': {'length': 4, 'difficulty': 'medium'}},
        'H': {'S': {'length': 5, 'difficulty': 'easy'}},
        'I': {'R': {'length': 3, 'difficulty': 'medium'}},
        'J': {'K': {'length': 2, 'difficulty': 'easy'}},
        'K': {'AA': {'length': 4, 'difficulty': 'easy'}, 'L': {'length': 17, 'difficulty': 'easy'}},
        'L': {'C': {'length': 2, 'difficulty': 'medium'}, 'M': {'length': 3, 'difficulty': 'medium'}},
        'M': {'O': {'length': 3, 'difficulty': 'medium'}, 'N': {'length': 10, 'difficulty': 'medium'}},
        'N': {'J': {'length': 5, 'difficulty': 'easy'}},
        'O': {'P': {'length': 3, 'difficulty': 'medium'}, 'Q': {'length': 9, 'difficulty': 'hard'}},
        'P': {'I': {'length': 4, 'difficulty': 'medium'}, 'G': {'length': 2, 'difficulty': 'medium'}},
        'Q': {'J': {'length': 3, 'difficulty': 'medium'}},
        'R': {'J': {'length': 2, 'difficulty': 'easy'}},
        'S': {'T': {'length': 3, 'difficulty': 'easy'}, 'X': {'length': 6, 'difficulty': 'easy'}},
        'T': {'R': {'length': 4, 'difficulty': 'easy'}, 'U': {'length': 2, 'difficulty': 'easy'}},
        'U': {'V': {'length': 1, 'difficulty': 'easy'}, 'J': {'length': 3, 'difficulty': 'easy'}},
        'V': {'K': {'length': 2, 'difficulty': 'medium'}},
        'W': {'S': {'length': 15, 'difficulty': 'easy'}, 'X': {'length': 17, 'difficulty': 'medium'}},
        'X': {'Y': {'length': 3, 'difficulty': 'easy'}},
        'Y': {'Z': {'length': 4, 'difficulty': 'easy'}},
        'Z': {'V': {'length': 3, 'difficulty': 'easy'}},
        'AA': {'A': {'length': 26, 'difficulty': 'easy'}}
    }
    
    #Heuristic function, for future*********
    def Heuristic(node1, node2):
        return 0  
    
    startingPointNode = ['X']
    nodesToVisit = ['H','P','D','N']
    allPermutations = PathFinder.GetAllPermutations(nodesToVisit)

    allPermutationsWithStartingNode = []

    for p in allPermutations:
        permWithStartingNode = startingPointNode + list(p)
        allPermutationsWithStartingNode.append(permWithStartingNode)
        #print(permWithStartingNode)

    shortestPathList = []

    shortestDisPathForEachPermDict = {}
    shortestPathListForEachPermList =[]
    
    

    for p in allPermutationsWithStartingNode:

        total_distance = 0
        total_path = []
        #print("--------------New perm_______________")
        #print("-----",p,"------")
        
        for i in range(len(p) - 1):
            pair = (p[i], p[i + 1])
            

            shortestDistancePathForCurrentPermutationDict = {}

            start_node, end_node = pair #Assigns the start and end node to the new pair

            #print("IN")
            #print(pair)
            shortestPathForCurrentPermutation = PathFinder.AStar(graph, start_node, end_node)
            #print(shortestPathForCurrentPermutation)
            #print("OUT")

            if shortestPathForCurrentPermutation is not None:
                distance = PathFinder.CalculateTotalDistance(shortestPathForCurrentPermutation, graph) #Calculates path distance for current pair in permutation

                shortestDistancePathForCurrentPermutationDict = {'distance': distance, 'path': shortestPathForCurrentPermutation}
                shortestPathList.append(shortestDistancePathForCurrentPermutationDict)

                total_distance += distance
                total_path.append(shortestPathForCurrentPermutation)    #Total current path to each pair in the permutation



    
        # Construct the dictionary
        shortestDisPathForEachPermDict = {'distance': total_distance, 'path': total_path}
        shortestPathListForEachPermList.append(shortestDisPathForEachPermDict)

        print("Total Distance: ", total_distance, "| Total Path: ", total_path)

    for key, value in shortestDisPathForEachPermDict.items():
        print(key, ":", value)



min_distance = float('inf')
min_path = None

# Iterate through each dictionary in the list
for shortestDisPathForEachPermDict in shortestPathListForEachPermList:

    distance = shortestDisPathForEachPermDict['distance']
    path = shortestDisPathForEachPermDict['path']

    # Compare distance with the current minimum distance
    if distance < min_distance:
        min_distance = distance 
        min_path = path
print("--------------------------------------------------------------------")
print("Smallest distance:", min_distance)
print("Corresponding path:", min_path)
print("--------------------------------------------------------------------")