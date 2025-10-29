namespace AdventOfCode2024
{
  class Day8
  {
    public static (int, int) Solve()
    {
      var matrix = Utils.ReadFileCharMatrix(8, false);
      var map = FindAntennae(matrix);
      HashSet<(int, int)> antiNodes = [];
      HashSet<(int, int)> antiNodes2 = [];

      foreach (var entry in map)
      {
        var pairs = GetPairs(entry.Value);
        foreach (var pair in pairs)
        {
          FindAntiNodeCoordinates(pair.Item1, pair.Item2, out var antiNode1, out var antiNode2);
          if (IsInBounds(antiNode1, matrix.GetLength(0), matrix.GetLength(1)))
          {
            antiNodes.Add(antiNode1);
          }
          if (IsInBounds(antiNode2, matrix.GetLength(0), matrix.GetLength(1)))
          {
            antiNodes.Add(antiNode2);
          }

          var antiNodesForPair = FindAntiNodeCoordinatesPart2(pair.Item1, pair.Item2, matrix.GetLength(0), matrix.GetLength(1));
          foreach (var antiNode in antiNodesForPair)
          {
            antiNodes2.Add(antiNode);
          }
        }
      }
      return (antiNodes.Count, antiNodes2.Count);
    }



    static Dictionary<char, List<(int, int)>> FindAntennae(char[,] matrix)
    {
      var result = new Dictionary<char, List<(int, int)>>();
      for (int i = 0; i < matrix.GetLength(0); i++)
      {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
          char freq = matrix[i, j];
          if (freq != '.')
          {
            result.TryGetValue(freq, out List<(int, int)>? antennae);
            if (antennae == null)
            {
              result[freq] = [(i, j)];
            }
            else
            {
              result[freq] = [.. antennae, (i, j)];
            }
          }
        }
      }
      return result;

    }

    static void FindAntiNodeCoordinates((int, int) a1, (int, int) a2, out (int, int) antiNode1, out (int, int) antiNode2)
    {
      var ySlope = a2.Item1 - a1.Item1;
      var xSlope = a2.Item2 - a1.Item2;
      antiNode1 = (a1.Item1 - ySlope, a1.Item2 - xSlope);
      antiNode2 = (a2.Item1 + ySlope, a2.Item2 + xSlope);
    }

    static List<(int, int)> FindAntiNodeCoordinatesPart2((int, int) a1, (int, int) a2, int len0, int len1)
    {
      var ySlope = a2.Item1 - a1.Item1;
      var xSlope = a2.Item2 - a1.Item2;
      var result = new List<(int, int)>([a1]);
      var i = 0;
      while (true)
      {
        var nextY = a1.Item1 - ySlope * i;
        var nextX = a1.Item2 - xSlope * i;
        if (IsInBounds((nextY, nextX), len0, len1))
        {
          result.Add((nextY, nextX));
        }
        else
        {
          break;
        }
        i++;
      }
      i = 0;
      while (true)
      {
        var nextY = a2.Item1 + ySlope * i;
        var nextX = a2.Item2 + xSlope * i;
        if (IsInBounds((nextY, nextX), len0, len1))
        {
          result.Add((nextY, nextX));
        }
        else
        {
          break;
        }
        i++;
      }
      return result;
    }


    static List<((int, int), (int, int))> GetPairs(List<(int, int)> coords)
    {
      var result = new List<((int, int), (int, int))>();
      for (int i = 0; i < coords.Count; ++i)
        for (int j = i + 1; j < coords.Count; ++j)
          result.Add((coords[i], coords[j]));
      return result;
    }

    static bool IsInBounds((int, int) coord, int len0, int len1)
    {
      return coord.Item1 >= 0 && coord.Item1 < len0 && coord.Item2 >= 0 && coord.Item2 < len1;
    }
  }
}
