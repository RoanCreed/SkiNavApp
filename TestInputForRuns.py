import json
import PathFinder_v2

file = open("NodesGraph.json")
NodesGraph = json.load(file)

file = open("RunsLiftsGraph.json")
RunsLiftsGraph = json.load(file)

#startingPointNode = 'f4946711-6818-4375-96ef-e487b025c61c' # lac blanc lift
startingPointNode = '2bda5768-f82a-404f-a1e1-2ccde0832c9a' # funitel pecelt start

#runsInput = ['Beranger','Christine','Croissant']
#runsInput = ['0602c22d0ee93ab4320c45ce4d9d3cea5b49f867', 'f9214995594b42205bf550a2ea2433ae66a4dbd0', 'a0bb99c174db2bf009db1d1dbf8b918fe0a16b4a']
runsInput = ['a0bb99c174db2bf009db1d1dbf8b918fe0a16b4a'] # croissant
#runsInput = ['327610f1acb523e9c5c26e69b849fb180f9939b7', 'c7ca163eb881f3d186a5467f6f5be8a102a4f1d5'] #lac blanc and beranger

weights = {
        "lift": 3.5,
        "novice": 1,
        "easy": 2,
        "intermediate": 3,
        "advanced": 4
    }


def GetStartEndPairs(runsInput, RunsLiftsGraph):
    startEndPairsList = []
    for runID in runsInput:
        if runID in RunsLiftsGraph:
            startNode = RunsLiftsGraph.get(runID).get("point_ids")[0]
            endNode = RunsLiftsGraph.get(runID).get("point_ids")[-1]
            startEndPairs = [startNode, endNode]
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

    selectedDefaultSkiRunsStartEndPairs = GetStartEndPairs(runsInput, RunsLiftsGraph)

    selectedDefaultSkiRunsPermutations = PathFinder_v2.GetAllPermutations(selectedDefaultSkiRunsStartEndPairs)

    appendedStartNodeToEachPermutation = AppendStartNodeToPermutations(selectedDefaultSkiRunsPermutations, startingPointNode)


    EndToStartPairs = []
    shortestPathList = []
    shortestDisPathForEachPermDict = {}
    shortestPathListForEachPermList = []


    for perm in appendedStartNodeToEachPermutation:
        totalDistance = 0
        totalPath = []
                                                #starting value of seq   |   length of list   |   increment
        for i in range(0, len(perm), 2):        #range(0,                |        len(perm)   |     , 2)
                
                
                
            if i + 1 < len(perm):
                pair = (perm[i], perm[i + 1])
                EndToStartPairs.append(pair)

                print("-----------------------Pair: " ,pair)
                    
                #Do Astar from here
                shortestPathForCurrentPermutation = PathFinder_v2.AStar(NodesGraph, perm[i], perm[i + 1], weights)
                #print("Shorted path for current permutation:" , shortestPathForCurrentPermutation)

                if shortestPathForCurrentPermutation is not None:
                    distance = PathFinder_v2.CalculateTotalDistance(shortestPathForCurrentPermutation, NodesGraph, weights) #Calculates path distance for current pair in permutation

                    shortestDistancePathForCurrentPermutationDict = {'distance': distance, 'path': shortestPathForCurrentPermutation}
                    shortestPathList.append(shortestDistancePathForCurrentPermutationDict)


                    totalPath.append(shortestPathForCurrentPermutation)    #Total current path to each pair in the permutation  
                    totalDistance += distance
                        
                    
                else:
                    print("There is no path")

                shortestDisPathForEachPermDict = {'distance': totalDistance, 'path': totalPath}
                shortestPathListForEachPermList.append(shortestDisPathForEachPermDict)

            else:
                #Add the last node after the Astar result TODO
                EndToStartPairs.append(perm[i]) #only adds one node (maybe insert this as a seperate var?)  

                
        print("Total Distance: ", totalDistance, "| Total Path: ", totalPath)
        
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