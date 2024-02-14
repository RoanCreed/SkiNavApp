import PathFinder


def GetSelectedSkiRuns(runsInput):
    selectedDefaultSkiRuns = []
    for runName in runsInput:
        #print(runName)
        if runName in defaultRuns:
            selectedDefaultSkiRuns.append({runName: defaultRuns[runName]})
            print({runName: defaultRuns[runName]})

    return selectedDefaultSkiRuns


if __name__ == "__main__":

    # graph = {
    #     'A': {'B': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 4, 'difficulty': 'easy'}},
    #     'B': {'A': {'length': 1, 'difficulty': 'easy'}, 'C': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 5, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
    #     'C': {'A': {'length': 4, 'difficulty': 'easy'}, 'B': {'length': 2, 'difficulty': 'easy'}, 'D': {'length': 1, 'difficulty': 'easy'}},
    #     'D': {'B': {'length': 5, 'difficulty': 'easy'}, 'C': {'length': 1, 'difficulty': 'easy'}, 'E': {'length': 10, 'difficulty': 'easy'}},
    #     'E': {'D': {'length': 2, 'difficulty': 'easy'}}
    # }


    nodeGraph = {
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


    #WITHOUT DIFFICULTY MULTIPLYERS ADDED
    #NODE ARE IN ORDER OF DOWNHILL
    defaultRuns = {
    'Beranger': {'nodes': {'A','F','D','G','I','R'},'totalRunLength': 24 },
    'Lac Blanc': {'nodes': {'A','B','C','D'},'totalRunLength': 13 },
    'Tete Ronde': {'nodes': {'A','E','W','S'},'totalRunLength': 24 },
    'Vires': {'nodes': {'B','L'},'totalRunLength': 7 },
    'Croissant': {'nodes': {'L','M','N'},'totalRunLength': 13 },
    'Corniche': {'nodes': {'N','J'},'totalRunLength': 5 },
    'Boulevard Lauzes': {'nodes': {'D','H'},'totalRunLength': 7 },
    'Trolles': {'nodes': {'P','G'},'totalRunLength': 2 },
    'Ardoises': {'nodes': {'G','H'},'totalRunLength': 3 },
    'Adrien Theaux': {'nodes': {'O','P','Q'},'totalRunLength': 3 },
    'BlackOQ': {'nodes': {'O','Q'},'totalRunLength': 9 },
    'Roc': {'nodes': {'R','J','K'},'totalRunLength': 4 },
    'Dalles': {'nodes': {'H','S','T','U','V'},'totalRunLength': 11 },
    'Christine': {'nodes': {'W','X'},'totalRunLength': 17 },
    '2 Combes': {'nodes': {'S','X'},'totalRunLength': 6 },
    'Combes de Thorens': {'nodes': {'X','Y','Z','V','K'},'totalRunLength': 12 },
    'RedLC': {'nodes': {'L','C'},'totalRunLength': 2 },
    'RedEF': {'nodes': {'E','F'},'totalRunLength': 6 },
    'BlueTR': {'nodes': {'T','R'},'totalRunLength': 4 },
    'GreenUJ': {'nodes': {'U','J'},'totalRunLength': 4 }
    }


    
    startingPointNode = ['K']

    runsInput = ['Beranger','Christine','Croissant']

    #nodesInput = ['R', 'Y', 'O','Q']
    #allPermutations = PathFinder.GetAllPermutations(nodesInput)

    selectedDefaultSkiRuns = []



    




    # for runName, runNodes in defaultRuns.items():
    #     print(runNodes)
    #     runStartNode = runNodes[0]  
    #     runEndNode = runNodes[-1]   
    #     print(f"Run: {runName}, Start Node: {runStartNode}, End Node: {runEndNode}")





    allPermutations = PathFinder.GetAllPermutations(runsInput)

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
            shortestPathForCurrentPermutation = PathFinder.AStar(nodeGraph, start_node, end_node)
            #print(shortestPathForCurrentPermutation)
            #print("OUT")

            if shortestPathForCurrentPermutation is not None:
                distance = PathFinder.CalculateTotalDistance(shortestPathForCurrentPermutation, nodeGraph) #Calculates path distance for current pair in permutation

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