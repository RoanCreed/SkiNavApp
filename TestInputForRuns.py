import json
import PathFinder_v2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

file = open("DataGraphs/NodesGraph.json")
NodesGraph = json.load(file)

file = open("DataGraphs/RunsLiftsGraph.json")
RunsLiftsGraph = json.load(file)

#startingPointNode = 'f4946711-6818-4375-96ef-e487b025c61c' # lac blanc lift
startingPointNode = '2bda5768-f82a-404f-a1e1-2ccde0832c9a' # funitel pecelt start

#runsInput = ['Beranger','Christine','Croissant']
#runsInput = ['0602c22d0ee93ab4320c45ce4d9d3cea5b49f867', 'f9214995594b42205bf550a2ea2433ae66a4dbd0', 'a0bb99c174db2bf009db1d1dbf8b918fe0a16b4a']
#runsInput = ['a0bb99c174db2bf009db1d1dbf8b918fe0a16b4a'] # croissant
runsInput = ['327610f1acb523e9c5c26e69b849fb180f9939b7', '0602c22d0ee93ab4320c45ce4d9d3cea5b49f867', 'a0bb99c174db2bf009db1d1dbf8b918fe0a16b4a'] #lac blanc and beranger, 

weights = {
        "lift": 1.4,
        "novice": 1,
        "easy": 1.2,
        "intermediate": 1.4,
        "advanced": 1.6
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

                print("-----------------------Pair: ", pair)
                    
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
                

            else:
                #Add the last node after the Astar result TODO
                EndToStartPairs.append(perm[i]) #only adds one node (maybe insert this as a seperate var?)  

                
        print("Total Distance: ", totalDistance, "| Total Path: ", totalPath)
        shortestPathListForEachPermList.append(shortestDisPathForEachPermDict)
        
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



# plot visited nodes
file = open("LocationGraph.json")
LocationGraph = json.load(file)

runsliftmap = pd.read_pickle("/Users/sebastian/Documents/SkiNavApp/runsliftmap.pkl")

def plot_visited_nodes(runsliftmap, runsInput, minPath, idx_nodes_start=None, idx_nodes_end=None):
    """
    runsliftmap: dataframe with all the runs as linestrings
    runsInput: selected runs
    minPath: shortes path found by Astar
    idx_nodes_start: the index of the first node that should be annotate on the map
    idx_nodes_end: the index of the last node that should be annotate on the map
    """
    if idx_nodes_start is None:
        idx_nodes_start = 0 
    if idx_nodes_end is None:
        idx_nodes_end = len(sum(minPath, []))

    visited_nodes = []
    for node in sum(minPath, []):
        visited_nodes.append(tuple(LocationGraph.get(node)))
    visited_nodes = np.asarray(visited_nodes)
    nodes_data = gpd.GeoDataFrame(visited_nodes, geometry=gpd.points_from_xy(visited_nodes[:,0], visited_nodes[:,1])).reset_index()
    
    fig, ax = plt.subplots(figsize=(12,14))
    runsliftmap.plot(ax=ax)
    runsliftmap[runsliftmap.id.isin(runsInput)].plot(ax=ax, color="lightgreen")
    nodes_data.geometry.plot(ax=ax, color="red")
    nodes_data.iloc[idx_nodes_start:idx_nodes_end].apply(lambda x: ax.annotate(text=x['index'], xy=x.geometry.centroid.coords[0], ha='right', size=8), axis=1)
    plt.show()


plot_visited_nodes(runsliftmap, runsInput, minPath, 0, 10) # change to number of nodes that should be annotated