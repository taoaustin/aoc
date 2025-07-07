namespace AdventOfCode2024
{
  class Day4
  {
    public static (int, int) Solve()
    {
      int xmasTally = 0;
      int masTally = 0;
      char[,] file = Utils.ReadFileCharMatrix(4);
      for (int i = 0; i < 4; i++)
      {
        for (int row = 0; row < file.GetLength(0); row++)
        {
          for (int col = 0; col < file.GetLength(1); col++)
          {
            if (IsForward(file, row, col)) xmasTally++;
            if (IsUpForward(file, row, col)) xmasTally++;
            if (IsCrossMAS(file, row, col)) masTally++;
          }
        }
        file = Utils.RotateMatrix90Clockwise(file);
      }
      return (xmasTally, masTally);
    }

    static bool IsForward(char[,] matrix, int row, int col)
    {
      if (col + 3 >= matrix.GetLength(1)) return false;
      char[] chars = [matrix[row, col], matrix[row, col + 1], matrix[row, col + 2], matrix[row, col + 3]];
      return new string(chars) == "XMAS";
    }

    static bool IsUpForward(char[,] matrix, int row, int col)
    {
      if ((row - 3 < 0) || (col + 3 >= matrix.GetLength(1))) return false;
      char[] chars = [matrix[row, col], matrix[row - 1, col + 1], matrix[row - 2, col + 2], matrix[row - 3, col + 3]];
      return new string(chars) == "XMAS";
    }

    static bool IsCrossMAS(char[,] matrix, int row, int col)
    {
      if (row - 1 < 0 || col - 1 < 0 || row + 1 >= matrix.GetLength(0) || col + 1 >= matrix.GetLength(1)) return false;
      return
        (matrix[row, col] == 'A') &&
        (matrix[row - 1, col - 1] == 'M') &&
        (matrix[row + 1, col - 1] == 'M') &&
        (matrix[row - 1, col + 1] == 'S') &&
        (matrix[row + 1, col + 1] == 'S');
    }
  }
}
