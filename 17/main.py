import math
import heapq

def get_i(vec, width): return vec[0] * width + vec[1]
def is_valid(vec, width, height):
    return vec[0] >= 0 and vec[0] < height and vec[1] >= 0 and vec[1] < width

def get_neighbours(v, dir, width, height, dir_times, min, max): 
    if v == 0:
        return ((1, (0, 1)), (width, (1, 0)))
    v_coord = (v // width, v % width)
    forward_v = (v_coord[0] + dir[0], v_coord[1] + dir[1])
    left_dir = (-dir[1], dir[0])
    left_v = (v_coord[0] + left_dir[0], v_coord[1] + left_dir[1])    
    right_dir = (dir[1], - dir[0])
    right_v = (v_coord[0] + right_dir[0], v_coord[1] + right_dir[1])    
    res = []
    if (dir_times < min):
        if (is_valid(forward_v, width, height)):
            res.append((get_i(forward_v, width), dir))
        return tuple(res)

    if (is_valid(forward_v, width, height) and dir_times < max):
        res.append((get_i(forward_v, width), dir))
    if (is_valid(left_v, width, height)):
        res.append((get_i(left_v, width), left_dir))
    if (is_valid(right_v, width, height)):
        res.append((get_i(right_v, width), right_dir))
    return tuple(res)

def dijkstra(graph, source, width, height, min, max):
    seen = set()
    dists = [math.inf for _ in range(len(graph))]
    pq = [(0, source, (0, 0), 0)]
    while pq:
        (dist, v, dir, dir_times) = heapq.heappop(pq)
        if (v, dir, dir_times) in seen:
            continue
        seen.add((v, dir, dir_times))
        for u, u_dir in get_neighbours(v, dir, width, height, dir_times, min, max):
            l_uv = graph[u]
            new_times = dir_times + 1 if u_dir == dir else 1
            if (l_uv + dist < dists[u] and new_times >= min):
                dists[u] = l_uv + dist
            heapq.heappush(pq, tuple((l_uv + dist, u, u_dir, new_times)))
    return dists[-1]

def main():
    lines = open("input.txt").read().splitlines()
    width = len(lines[0])
    edge_weights = [int(c) for line in lines for c in line]
    silver = dijkstra(edge_weights, 0, width, len(lines), 1, 3)
    print(f"Part 1: {silver}")
    gold = dijkstra(edge_weights, 0, width, len(lines), 4, 10)
    print(f"Part 2: {gold}")
     
if __name__ == "__main__":
    main()
    # Ended up being more like dp than greedy dijkstra :/
    # Can't mark a vertex as visited (seen). 
    # But you can mark a state: (vertex, prev-direction, #-of-times-of-prev-direction) visited.
