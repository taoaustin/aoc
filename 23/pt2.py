from typing import List, Tuple

def construct_graph(grid): # start nodes at (0, 1)
    grid = [line[:] for line in grid]

    # finding nodes
    nodes = [[]]
    grid[0][1] = '0'
    node_idx = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            deg = 0
            for d_r, d_c in directions:
                if i + d_r > 0 and i + d_r < len(grid) and j + d_c > 0 and j + d_c < len(grid[i]):
                    if grid[i][j] == "." and grid[i + d_r][j + d_c] == "v" or grid[i + d_r][j + d_c] == ">": deg += 1
            if deg > 1:
                grid[i][j] = str(node_idx)
                node_idx += 1
                nodes.append([])
    grid[-1][-2] = str(node_idx)
    nodes.append([])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "v" or grid[i][j] == ">":
                grid[i][j] = "."
    
    # build adjacency list
    q: List[Tuple[int, int, int]] = [(0, 0, 1)]
    while q:
        n, n_row, n_col = q.pop(0)
        out_paths = []
        if n_row + 1 < len(grid) and grid[n_row + 1][n_col] == ".": out_paths.append((n_row + 1, n_col))
        if n_col + 1 < len(grid[0]) and grid[n_row][n_col + 1] == ".": out_paths.append((n_row, n_col + 1))
        if n_row - 1 >= 0 and grid[n_row - 1][n_col] == ".": out_paths.append((n_row - 1, n_col))
        if n_col - 1 >= 0 and grid[n_row][n_col - 1] == ".": out_paths.append((n_row, n_col - 1))
        for o_path in out_paths:
            p_len = 1
            r, c = o_path
            while not grid[r][c].isnumeric():
                grid[r][c] = "X"
                for d_r, d_c in directions:
                    if r + d_r >= 0 and r + d_r < len(grid) and c + d_c >= 0 and c + d_c < len(grid[r]):
                        if grid[r + d_r][c + d_c] != "#" and grid[r + d_r][c + d_c] != "X" and grid[r + d_r][c + d_c] != str(n):
                            r, c = r + d_r, c + d_c
                            p_len += 1
                            break
            q.append((int(grid[r][c]), r, c))
            nodes[n].append((int(grid[r][c]), p_len))
            nodes[int(grid[r][c])].append((n, p_len))
    return nodes


def get_max_path(u, v, cur_len):
    if visited[u]:
        return
    visited[u] = True
    if u == v:
        all_path_lens.append(cur_len)
        visited[u] = False
        return
    for neighbour in graph[u]:
        get_max_path(neighbour[0], v, cur_len + neighbour[1])
    visited[u] = False

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
grid = [list(line) for line in open("input.txt").read().splitlines()]
graph = construct_graph(grid)
visited = [False for _ in range(len(graph))]
all_path_lens = []
get_max_path(0, len(graph) - 1, 0)
gold = max(all_path_lens)
print(f"Part 2: {gold}")
# basically brute force... but still finishes under a minute 








