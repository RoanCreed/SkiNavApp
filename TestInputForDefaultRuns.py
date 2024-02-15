import PathFinder


def GetSelectedSkiRuns(runsInput, defaultRuns):  #Loops through list of selected runs and takes their information from the dictionary
    selectedDefaultSkiRuns = []
    for runName in runsInput:
        #print(runName)
        if runName in defaultRuns:
            selectedDefaultSkiRuns.append({runName: defaultRuns[runName]})
            print({runName: defaultRuns[runName]})

    return selectedDefaultSkiRuns


def GetStartEndPairs(selectedDefaultSkiRuns):
    startEndPairsList = []
    for run in selectedDefaultSkiRuns:  #loop each run inside the selected runs list
        runName = next(iter(run))   #Takes the first key in the dictionary and asigns it to key 'runName' ('Croissant')
        runDict = run[runName]      #Uses the run name to extract the internal dictionary for that run (nodes and length)

        nodesList = list(runDict['nodes'])    #Get nodes from each inner dictionary in each run list entry

        startNode = nodesList[0]
        endNode = nodesList[-1]
        startEndPairs = [startNode, endNode]

        #print(startEndPairs)
        startEndPairsList.append(startEndPairs)
        
    return startEndPairsList


def AppendStartNodeToPermutations(permutations, startingNode):
    AppendedPermutationsList = []
    for permutation in permutations:
        sumPerms = sum(permutation, [])
        sumPerms.insert(0,startingNode)
        AppendedPermutationsList.append(sumPerms)

    return AppendedPermutationsList



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
    'Beranger': {'nodes': ['A', 'F', 'D', 'G', 'I', 'R'], 'totalRunLength': 24},
    'Lac Blanc': {'nodes': ['A', 'B', 'C', 'D'], 'totalRunLength': 13},
    'Tete Ronde': {'nodes': ['A', 'E', 'W', 'S'], 'totalRunLength': 24},
    'Vires': {'nodes': ['B', 'L'], 'totalRunLength': 7},
    'Croissant': {'nodes': ['L', 'M', 'N'], 'totalRunLength': 13},
    'Corniche': {'nodes': ['N', 'J'], 'totalRunLength': 5},
    'Boulevard Lauzes': {'nodes': ['D', 'H'], 'totalRunLength': 7},
    'Trolles': {'nodes': ['P', 'G'], 'totalRunLength': 2},
    'Ardoises': {'nodes': ['G', 'H'], 'totalRunLength': 3},
    'Adrien Theaux': {'nodes': ['O', 'P', 'Q'], 'totalRunLength': 3},
    'BlackOQ': {'nodes': ['O', 'Q'], 'totalRunLength': 9},
    'Roc': {'nodes': ['R', 'J', 'K'], 'totalRunLength': 4},
    'Dalles': {'nodes': ['H', 'S', 'T', 'U', 'V'], 'totalRunLength': 11},
    'Christine': {'nodes': ['W', 'X'], 'totalRunLength': 17},
    '2 Combes': {'nodes': ['S', 'X'], 'totalRunLength': 6},
    'Combes de Thorens': {'nodes': ['X', 'Y', 'Z', 'V', 'K'], 'totalRunLength': 12},
    'RedLC': {'nodes': ['L', 'C'], 'totalRunLength': 2},
    'RedEF': {'nodes': ['E', 'F'], 'totalRunLength': 6},
    'BlueTR': {'nodes': ['T', 'R'], 'totalRunLength': 4},
    'GreenUJ': {'nodes': ['U', 'J'], 'totalRunLength': 4}
    }


    
    startingPointNode = 'K'

    runsInput = ['Beranger','Christine','Croissant']

    #nodesInput = ['R', 'Y', 'O','Q']
    #allPermutations = PathFinder.GetAllPermutations(nodesInput)

    #selectedDefaultSkiRuns = []

    selectedDefaultSkiRuns = GetSelectedSkiRuns(runsInput, defaultRuns)
    #print("selected ski runs: ", selectedDefaultSkiRuns)

    selectedDefaultSkiRunsStartEndPairs = GetStartEndPairs(selectedDefaultSkiRuns)
    #print("Selected ski run pairs:",selectedDefaultSkiRunsStartEndPairs)

    selectedDefaultSkiRunsPermutations = PathFinder.GetAllPermutations(selectedDefaultSkiRunsStartEndPairs)
    #print(selectedDefaultSkiRunsPermutations)

    appendedStartNodeToEachPermutation = AppendStartNodeToPermutations(selectedDefaultSkiRunsPermutations, startingPointNode)

    EndToStartPairs = []

    

    shortestPathList = []
    shortestDisPathForEachPermDict = {}
    shortestPathListForEachPermList = []
    

    for perm in appendedStartNodeToEachPermutation:
        totalDistance = 0
        total_path = []
                                            #starting value of seq   |   length of list   |   increment
        for i in range(0, len(perm), 2):    #range(0,          |        len(perm)       |     , 2)
            
            
            
            if i + 1 < len(perm):
                pair = (perm[i], perm[i + 1])
                EndToStartPairs.append(pair)

                print("-----------------------Pair: " ,pair)
                
                #Do Astar from here
                shortestPathForCurrentPermutation = PathFinder.AStar(nodeGraph, perm[i], perm[i + 1])
                #print("Shorted path for current permutation:" , shortestPathForCurrentPermutation)

                if shortestPathForCurrentPermutation is not None:
                    distance = PathFinder.CalculateTotalDistance(shortestPathForCurrentPermutation, nodeGraph) #Calculates path distance for current pair in permutation

                    shortestDistancePathForCurrentPermutationDict = {'distance': distance, 'path': shortestPathForCurrentPermutation}
                    shortestPathList.append(shortestDistancePathForCurrentPermutationDict)


                    total_path.append(shortestPathForCurrentPermutation)    #Total current path to each pair in the permutation  
                    totalDistance += distance
                    
                
                else:
                    print("There is no path")

                shortestDisPathForEachPermDict = {'distance': totalDistance, 'path': total_path}
                shortestPathListForEachPermList.append(shortestDisPathForEachPermDict)

            else:
                #Add the last node after the Astar result TODO
                EndToStartPairs.append(perm[i]) #only adds one node (maybe insert this as a seperate var?)  

            
            


        

        print("Total Distance: ", totalDistance, "| Total Path: ", total_path)
    
        for key, value in shortestDisPathForEachPermDict.items():
            print(key, ":", value)



minDistance = float('inf')
minPath = None

# Iterate through each dictionary in the list
for shortestDisPathForEachPermDict in shortestPathListForEachPermList:

    distance = shortestDisPathForEachPermDict['distance']
    path = shortestDisPathForEachPermDict['path']

    # Compare distance with the current minimum distance
    if distance < minDistance:
        minDistance = distance 
        minPath = path
print("--------------------------------------------------------------------")
print("Smallest distance:", minDistance)
print("Corresponding path:", minPath)
print("--------------------------------------------------------------------")
    
    