from typing import List, Tuple

def print_graph(grid):
    for line in grid:
        print("".join(line))

# using bfs
def construct_graph(grid): # start nodes at (0, 1)
    grid = [line[:] for line in grid]

    # finding nodes
    nodes = [[]]
    grid[0][1] = '0'
    grid[1][1] = 'v'
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
    grid[-2][-2] = 'v'
    nodes.append([])
    
    # build adjacency list
    q: List[Tuple[int, int, int]] = [(0, 0, 1)]
    while q:
        n, n_row, n_col = q.pop(0)
        out_paths = []
        if n_row + 1 < len(grid) and grid[n_row + 1][n_col] == "v": out_paths.append((n_row + 1, n_col))
        if n_col + 1 < len(grid[0]) and grid[n_row][n_col + 1] == ">": out_paths.append((n_row, n_col + 1))
        for o_path in out_paths:
            p_len = 2
            r, c = o_path
            grid[r][c] = "X"
            while grid[r][c] != ">" and grid[r][c] != "v":
                grid[r][c] = "X"
                for d_r, d_c in directions:
                    if r + d_r > 0 and r + d_r < len(grid) and c + d_c > 0 and c + d_c < len(grid[r]):
                        if grid[r + d_r][c + d_c] != "#" and grid[r + d_r][c + d_c] != "X":
                            r, c = r + d_r, c + d_c
                            p_len += 1
                            break
            if grid[r][c] == "v":
                q.append((int(grid[r + 1][c]), r + 1, c))
                nodes[n].append((int(grid[r + 1][c]), p_len))
            if grid[r][c] == ">":
                q.append((int(grid[r][c + 1]), r, c + 1))
                nodes[n].append((int(grid[r][c + 1]), p_len))
            grid[r][c] = "X"
    return nodes

def topological_sort(graph):
    l = []
    visited = set()
    not_visited = set(i for i in range(len(graph)))
    tmp_visited = set()
    def visit(n):
        if n in visited: return
        if n in tmp_visited:
            print("ERROR, THERE IS A CYCLE, GRAPH IS NOT A DAG")
            return
        tmp_visited.add(n)
        for m, _ in graph[n]: visit(m)
        tmp_visited.remove(n)
        visited.add(n)
        not_visited.remove(n)
        l.insert(0, n)
    while (len(not_visited) != 0):
        visit(next(iter(not_visited)))
    return l

def get_longest_path(graph, ordering):
    dp = [0 for _ in range(len(graph))]
    for n in ordering:
        max_d = 0
        for i, v in enumerate(graph):
            for e, e_d in v:
                if e == n:
                    max_d = max(max_d, dp[i] + e_d)
        dp[n] = max_d
    return dp[-1]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
grid = [list(line) for line in open("input.txt").read().splitlines()]
graph = construct_graph(grid)
topological_ordering = topological_sort(graph)
silver = get_longest_path(graph, topological_ordering)
print(f"Part 1: {silver}")
# we can use the fact that the graph is a DAG to create a linear-time solution for part 1.
# since for part 2 we remove that assumption the solution is NP-hard (unless im missing some other assumption)
# more importantly it makes all my code for part 1 not reusable :/

