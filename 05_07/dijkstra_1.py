import heapq


INF = float("infinity")

# Define graph as dictionary representing adjacency list.
graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10}
}
# [('U', 0), ('V', 6), ('W', 7), ('X', 8)]


# graph = {
#     "A": {"B": 6, "D": 1},
#     "B": {"A": 6, "C": 5, "D": 2, "E": 2},
#     "C": {"B": 5, "E": 5},
#     "D": {"A": 1, "B": 2, "E": 1},
#     "E": {"B": 2, "C": 5, "D": 1}
# }
# [('A', 0), ('B', 3), ('C', 7), ('D', 1), ('E', 2)]


unvisited_min_distances = {vertex: INF for vertex in graph}
visited_vertices = {}
current_vertex = "U"  # The start node.
unvisited_min_distances[current_vertex] = 0

# While vertices remain unvisited
while len(unvisited_min_distances) > 0:
    # Visit unvisited vertex with smallest known distance from start vertex.
    current_vertex, current_distance = sorted(unvisited_min_distances.items(), key=lambda x: x[1])[
        0]  # Very inefficient - use priority queue in "real" version.
    # For each unvisited neighbour of the current vertex
    for neighbour, neighbour_distance in graph[current_vertex].items():
        # If a neighbour has been processed, skip it.
        if neighbour in visited_vertices:
            continue
        # Calculate the new distance if this route is taken.
        potential_new_distance = current_distance + neighbour_distance
        # If the calculated distance of this vertex is less than the known distance
        if potential_new_distance < unvisited_min_distances[neighbour]:
            # Update the distance for this neighbour.
            unvisited_min_distances[neighbour] = potential_new_distance
    # Add the current vertex to the visited vertices.
    visited_vertices[current_vertex] = current_distance
    # Remove the current vertex from the unvisited list (dictionary).
    del unvisited_min_distances[current_vertex]


def shortest_path_dijkistra(graph, u):
    distances = {vertex: INF for vertex in graph}
    distances[u] = 0
    pq = [(0, u)]

    while len(pq) > 0:
        current_dist, current_vertex = heapq.heappop(pq)

        if current_dist > distances[current_vertex]:
            continue

        for neighbour, neighbour_dist in graph[current_vertex].items():
            distance = current_dist + neighbour_dist

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return distances


# Display results.
print(sorted(visited_vertices.items()))
print(shortest_path_dijkistra(graph, "U"))
