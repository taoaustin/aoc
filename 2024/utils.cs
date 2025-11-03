namespace AdventOfCode2024
{
  class Utils
  {
    public static string ReadFileString(int day, bool test = false)
    {
      return File.ReadAllText(GetInputFile(day, test));
    }

    public static string[] ReadFileLines(int day, bool test = false)
    {
      return File.ReadAllLines(GetInputFile(day, test));
    }

    public static char[][] ReadFileChar2DArray(int day, bool test = false)
    {
      return [.. ReadFileLines(day, test).Select(line => line.ToCharArray())];
    }

    public static char[,] ReadFileCharMatrix(int day, bool test = false)
    {
      return Convert2DArrToMatrix(ReadFileChar2DArray(day, test));
    }

    public static T[,] RotateMatrix90Clockwise<T>(T[,] matrix)
    {
      int rows = matrix.GetLength(0);
      int cols = matrix.GetLength(1);
      T[,] rotated = new T[cols, rows];

      for (int i = 0; i < rows; i++)
      {
        for (int j = 0; j < cols; j++)
        {
          rotated[j, rows - 1 - i] = matrix[i, j];
        }
      }
      return rotated;
    }

    public static T[,] Convert2DArrToMatrix<T>(T[][] arr2D)
    {
      if (arr2D == null || arr2D.Length == 0)
        throw new ArgumentException("Invalid 2D array");

      int rows = arr2D.Length;
      int cols = arr2D[0].Length;

      if (arr2D.Any(row => row.Length != cols))
        throw new ArgumentException("All rows must have the same length");

      var rectArray = new T[rows, cols];

      foreach (var (row, i) in arr2D.Select((r, i) => (r, i)))
      {
        foreach (var (c, j) in row.Select((c, j) => (c, j)))
        {
          rectArray[i, j] = c;
        }
      }
      return rectArray;
    }

    public static bool InRange<T>((int, int) coord, T[,] matrix)
    {
      return coord.Item1 >= 0 && coord.Item1 < matrix.GetLength(0) && coord.Item2 >= 0 && coord.Item2 < matrix.GetLength(1);
    }

    public static (int, int)[] AdjacentCoords((int, int) coord)
    {
      var (a, b) = coord;
      return [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)];
    }

    static string GetInputFile(int i, bool test = false)
    {
      return $"{i:D2}/input{(test ? "_test" : "")}.txt";
    }
  }
}
