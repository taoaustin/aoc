namespace AdventOfCode2024
{
  class Day10
  {
    public static (int, int) Solve()
    {
      var matrix = Utils.Convert2DArrToMatrix(
          Utils.ReadFileChar2DArray(10, false).Select(row => row.Select(c => c - '0').ToArray()).ToArray()
          );

      var trailHeads = FindTrailHeads(matrix);
      var part1 = 0;
      var part2 = 0;
      foreach (var trailHead in trailHeads)
      {
        var score = Score(matrix, trailHead, true);
        var score2 = Score(matrix, trailHead, false);
        part1 += score;
        part2 += score2;
      }
      return (part1, part2);
    }

    static (int, int)[] FindTrailHeads(int[,] matrix)
    {
      List<(int, int)> result = [];
      for (int i = 0; i < matrix.GetLength(0); i++)
      {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
          if (matrix[i, j] == 0)
          {
            result.Add((i, j));
          }
        }
      }
      return [.. result];
    }


    static int Score(int[,] matrix, (int, int) trailhead, bool useVisited) //bfs
    {

      var score = 0;
      Queue<(int, int)> q = new([trailhead]);
      HashSet<(int, int)> visited = [trailhead];
      while (q.Count > 0)
      {
        var coord = q.Dequeue();
        var val = matrix[coord.Item1, coord.Item2];
        if (val == 9)
        {
          score++;
          continue;
        }
        var adjacent = Utils.AdjacentCoords(coord).Where(item => Utils.InRange(item, matrix));
        foreach (var a in adjacent)
        {
          if (useVisited && !visited.Contains(a) && matrix[a.Item1, a.Item2] == val + 1)
          {
            q.Enqueue(a);
            visited.Add(a);
          }
          else if (!useVisited && matrix[a.Item1, a.Item2] == val + 1)
          {
            q.Enqueue(a);
          }
        }
      }
      return score;
    }
  }
}
