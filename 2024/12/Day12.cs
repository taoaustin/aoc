namespace AdventOfCode2024
{
  class Day12
  {
    public static (int, int) Solve()
    {
      var grid = Utils.ReadFileCharMatrix(12, false);
      var visited = new HashSet<(int, int)>();
      var p1Price = 0;
      var p2Price = 0;
      for (int i = 0; i < grid.GetLength(0); i++)
      {
        for (int j = 0; j < grid.GetLength(1); j++)
        {
          if (!visited.Contains((i, j)))
          {
            var (area, perim, vertices) = BFS((i, j), grid, visited);
            p1Price += area * perim;
            p2Price += area * vertices;
          }
        }
      }
      return (p1Price, p2Price);
    }

    static (int, int, int) BFS((int, int) start, char[,] grid, HashSet<(int, int)> visited)
    {
      visited.Add(start);
      var (row, col) = start;
      var c = grid[row, col];

      int area = 0;
      int perimeter = 0;
      int vertices = 0;
      var q = new Queue<(int, int)>([start]);
      while (q.Count != 0)
      {
        var coord = q.Dequeue();
        area++;
        var adjacents = Utils.AdjacentCoords(coord);
        var edges = new List<(int, int)>();
        foreach (var (i, j) in adjacents)
        {
          if (!Utils.InRange((i, j), grid) || grid[i, j] != c)
          {
            edges.Add((i, j));
          }
          if (!visited.Contains((i, j)) && Utils.InRange((i, j), grid) && grid[i, j] == c)
          {
            visited.Add((i, j));
            q.Enqueue((i, j));
          }
        }
        perimeter += edges.Count;

        // convex vertices
        if (edges.Count > 1)
        {
          var invalidAdjacentPairs = Utils.GetPairs(edges);
          foreach (var pair in invalidAdjacentPairs)
          {
            if (Utils.IsDiagonallyAdjacent(pair.Item1, pair.Item2)) vertices++;
          }
        }

        // concave vertices
        var validAdjacents = adjacents.Where(coord => Utils.InRange(coord, grid) && grid[coord.Item1, coord.Item2] == c);
        var diagAdjacents = Utils.DiagonallyAdjacentCoords(coord).Where(coord => Utils.InRange(coord, grid) && grid[coord.Item1, coord.Item2] != c);
        foreach (var (i, j) in diagAdjacents)
        {
          var intersect = validAdjacents.Intersect(Utils.AdjacentCoords((i, j)));
          if (intersect.Count() == 2) vertices++;
        }
      }
      return (area, perimeter, vertices);
    }
  }
}
