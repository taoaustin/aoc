import math
import heapq

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

def left_of(vec_row, vec_col): return (-vec_col, vec_row)
def right_of(vec_row, vec_col): return (vec_col, -vec_row)
def get_i(vec_row, vec_col, width): return vec_row * width + vec_col
def get_coord(i, width): return (i // width, i % width)
def is_valid_coord(vec_row, vec_col, width, height):
    return vec_row >= 0 and vec_row < height and vec_col >= 0 and vec_col < width
def add_coord(x, y): return tuple(map(lambda i, j: i + j, x, y))

def get_neighbours(v, dir, width, height, dir_times, min, max): 
    if v == 0:
        return ((1, RIGHT), (width, DOWN))
    v_coord = get_coord(v, width)
    forward_v = add_coord(v_coord, dir)
    left_dir = left_of(*dir)
    left_v = add_coord(v_coord, left_dir)
    right_dir = right_of(*dir)
    right_v = add_coord(v_coord, right_dir)
    res = []
    if (dir_times < min):
        if (is_valid_coord(forward_v[0], forward_v[1], width, height)):
            res.append((get_i(forward_v[0], forward_v[1], width), dir))
        return tuple(res)

    if (is_valid_coord(forward_v[0], forward_v[1], width, height) and dir_times < max):
        res.append((get_i(forward_v[0], forward_v[1], width), dir))
    if (is_valid_coord(left_v[0], left_v[1], width, height)):
        res.append((get_i(left_v[0], left_v[1], width), left_dir))
    if (is_valid_coord(right_v[0], right_v[1], width, height)):
        res.append((get_i(right_v[0], right_v[1], width), right_dir))
    return tuple(res)

def dijkstra(graph, source, width, height, min, max):
    seen = set()
    dists = [math.inf for _ in range(len(graph))]
    pq = [(0, source, (0, 0), 0)]
    while pq:
        v_tup = heapq.heappop(pq)
        (dist, v, dir, dir_times) = v_tup
        if (dir_times, v, dir) in seen:
            continue
        seen.add((dir_times, v, dir))
        for u, u_dir in get_neighbours(v, dir, width, height, dir_times, min, max):
            l_uv = graph[u]
            if (u_dir == dir): new_times = dir_times + 1
            else: new_times = 1
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
