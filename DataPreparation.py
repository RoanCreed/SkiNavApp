import json
import uuid
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString
from data_models import CreateBaseRunsLiftsGraph, GetConnections, CreateRunsLiftsGraph, CreateLocationGraph, CreateRunsLiftsNodesGraph, CreateNodesGraph

dir = "/Users/sebastian/Documents/SkiNavApp/"
dir_tmp = "/Users/sebastian/Documents/SkiNavApp_tmp/"

gdf_runs = pd.read_pickle(dir_tmp+"runs_les_trois_vallee.pkl")
gdf_lifts = pd.read_pickle(dir_tmp+"lifts_les_trois_vallee.pkl")

# change to crs france UoM metric
features = ["id", "name", "resort_name", "connection_type", "difficulty",
            "duration", "distance", "geometry", "start", "end"]

gdf_runs = gdf_runs.to_crs("27561")
gdf_runs["uses"] = gdf_runs.uses.apply(lambda x: x[0])
gdf_runs["distance"] = gdf_runs.geometry.length
gdf_runs["start"] = gdf_runs.geometry.apply(lambda x: Point(x.coords[0]))
gdf_runs["end"] = gdf_runs.geometry.apply(lambda x: Point(x.coords[-1]))
gdf_runs["connection_type"] = "run"
gdf_runs["duration"] = gdf_runs["distance"] / 7 # 25km/h or 7m/s
gdf_runs = gdf_runs[gdf_runs.uses=="downhill"]
gdf_runs = gdf_runs[features]

# change to crs france UoM metric
gdf_lifts = gdf_lifts.to_crs("27561")
gdf_lifts["distance"] = gdf_lifts.geometry.length
gdf_lifts["start"] = gdf_lifts.geometry.apply(lambda x: Point(x.coords[0]))
gdf_lifts["end"] = gdf_lifts.geometry.apply(lambda x: Point(x.coords[-1]))
gdf_lifts["geometry"] = gdf_lifts.geometry.apply(lambda x: LineString([x.coords[0], x.coords[-1]]))
gdf_lifts["connection_type"] = "lift"
gdf_lifts = gdf_lifts.rename(columns={"liftType": "lift_type"})
gdf_lifts.head()
gdf_lifts["difficulty"] = "lift"
mean_speed = gdf_lifts[gdf_lifts["duration"].notnull()]["distance"].sum() / gdf_lifts[gdf_lifts["duration"].notnull()].duration.sum()
gdf_lifts["duration"] = np.where(gdf_lifts["duration"].isna(), (gdf_lifts["distance"] / mean_speed), gdf_lifts["duration"])
gdf_lifts = gdf_lifts[features]

data = pd.concat([gdf_lifts, gdf_runs])

# define subsample if intended
data = data[~((data["name"].isin(["Stade"])) & (data.connection_type=="lift")) & (data.geometry.apply(lambda x: x.coords[0][1]) < -257000) & (data.geometry.apply(lambda x: x.coords[0][1]) > -260000) & (data.geometry.apply(lambda x: x.coords[0][0]) > 933000)]
data = data[~data.id.isin(["4c8d28e91232c0842a7ee27b6b688f83e36871c1", "8ca54533ba58833bb34bf182c41401bcc6ff564e"])]
data.geometry.plot()


points = data.geometry.apply(lambda x: x.coords).rename("point").explode().reset_index().rename(columns={"index": "Index"})
data = data.reset_index().rename(columns={"index": "Index"})

unique_id = []
for i in range(len(points)):
    unique_id.append(str(uuid.uuid4()))

points["point_id"] = unique_id
points = points.merge(data[["id", "name", "Index", "difficulty", "duration", "distance", "connection_type", "start", "end"]], how="left", on="Index")
points = gpd.GeoDataFrame(points, geometry=[Point(x) for x in points.point]).rename(columns={"id": "run_id"})

start_points = points.groupby("run_id").first().reset_index()
start_points["point_type"] = "start"
end_points = points.groupby("run_id").last().reset_index()
end_points["point_type"] = "end"
start_end_points = pd.concat([start_points, end_points], axis=0).sort_values(by="run_id")
points["points_by_run"] = points.groupby("run_id").point_id.transform("count")


# create runsliftsgraph
RunsLiftsGraph = CreateBaseRunsLiftsGraph(points)

# get connected points and assing new unique node it
RunsLiftsGraph_tmp = GetConnections(RunsLiftsGraph, start_end_points)

# create RunsLiftsGraph
RunsLiftsGraph = CreateRunsLiftsGraph(RunsLiftsGraph_tmp)

# create LocationGraph
LocationGraph = CreateLocationGraph(RunsLiftsGraph_tmp)

# iterate through RunLifts, calculate segment length and keep nodes, start and end points
RunsLiftsNodesGraph = CreateRunsLiftsNodesGraph(RunsLiftsGraph_tmp)

# create NodesGraph
NodesGraph = CreateNodesGraph(RunsLiftsNodesGraph)


with open ("RunsLiftsGraph.json", "w") as file:
    file.write(json.dumps(RunsLiftsGraph))

with open ("LocationGraph.json", "w") as file:
    file.write(json.dumps(LocationGraph))

with open ("NodesGraph.json", "w") as file:
    file.write(json.dumps(NodesGraph))

print("SUCCESS")