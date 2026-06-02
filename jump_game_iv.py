def minJumps(arr: list[int]) -> int:
    all_jumps = []
    for i in range(len(arr)):
        current_possible_jumps = set()
        if i + 1 < len(arr):
            current_possible_jumps.add(i + 1)
        if i - 1 >= 0:
            current_possible_jumps.add(i - 1)
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                current_possible_jumps.add(j)
        all_jumps.append(list(current_possible_jumps))

    return len(dijkstra(all_jumps)) - 1


def dijkstra(graph: list[list[int]]) -> list[int]:
    src = 0
    dest = len(graph) - 1
    unvisited = set([i for i in range(len(graph))])
    predecessors = {}
    distances = {}

    for node in unvisited:
        distances[node] = float("inf")
    distances[src] = 0

    while len(unvisited) > 0:
        node = next_nearest_node(distances, unvisited)
        unvisited.remove(node)

        if node == dest:
            return get_path(dest, predecessors)

        for neighbour in graph[node]:
            if neighbour not in unvisited:
                continue
            known_distance = distances[node]
            distance_to_src = known_distance + 1
            if distance_to_src < distances[neighbour]:
                distances[neighbour] = distance_to_src
                predecessors[neighbour] = node

    return get_path(dest, predecessors)


def get_path(dest: int, predecessors: dict[int, int]) -> list[int]:
    path = []
    pred = dest

    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)

    path.reverse()
    return path


def next_nearest_node(distances: dict[int, int], unvisited) -> int:
    min_dist = float("inf")
    next_nearest = -1
    for node in unvisited:
        distance_so_far = distances[node]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            next_nearest = node

    return next_nearest


print(minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
