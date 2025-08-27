namespace AdventOfCode2024
{
  class Day6
  {
    enum Direction
    {
      Up,
      Down,
      Left,
      Right
    }

    public static (int, int) Solve()
    {
      char[,] maze = Utils.ReadFileCharMatrix(6);
      (int row, int col) = FindStartPosition(maze);
      var traveled = Travel(maze, row, col);
      var newObstacles = CheckForLoops(maze, row, col, traveled);
      return (traveled.Count, newObstacles);
    }

    static HashSet<(int, int)> Travel(char[,] maze, int row, int col)
    {
      Direction dir = Direction.Up;
      HashSet<(int, int)> hashset = [(row, col)];
      while (InBounds(maze, row, col))
      {
        hashset.Add((row, col));
        if (CanMove(maze, dir, row, col)) (row, col) = Move(dir, row, col);
        else dir = Turn(dir);
      }
      return hashset;
    }

    static int CheckForLoops(char[,] maze, int row, int col, HashSet<(int, int)> traveled)
    {
      var count = 0;
      foreach ((int i, int j) in traveled)
      {
        if ((i, j) == (row, col)) continue;
        var copy = new char[maze.GetLength(0), maze.GetLength(1)];
        Array.Copy(maze, copy, maze.Length);
        copy[i, j] = '#';
        if (HasLoop(copy, row, col)) count++;
      }
      return count;
    }


    static bool HasLoop(char[,] maze, int row, int col)
    {
      Direction dir = Direction.Up;
      HashSet<(int, int, Direction)> hashset = [];
      while (InBounds(maze, row, col))
      {
        if (hashset.Contains((row, col, dir))) return true;
        hashset.Add((row, col, dir));
        if (CanMove(maze, dir, row, col)) (row, col) = Move(dir, row, col);
        else dir = Turn(dir);
      }
      return false;
    }




    static bool CanMove(char[,] maze, Direction dir, int row, int col, bool mustBeInBounds = false)
    {
      (row, col) = Move(dir, row, col);
      if (!mustBeInBounds) return !InBounds(maze, row, col) || maze[row, col] != '#';
      return InBounds(maze, row, col) && maze[row, col] != '#';
    }

    static (int, int) Move(Direction dir, int row, int col)
    {
      return dir switch
      {
        Direction.Up => (row - 1, col),
        Direction.Down => (row + 1, col),
        Direction.Left => (row, col - 1),
        Direction.Right => (row, col + 1),
        _ => (row, col),
      };
    }

    static bool InBounds(char[,] maze, int row, int col)
    {
      return row >= 0 && row < maze.GetLength(0) && col >= 0 && col < maze.GetLength(1);
    }

    static Direction Turn(Direction dir)
    {
      return dir switch
      {
        Direction.Up => Direction.Right,
        Direction.Down => Direction.Left,
        Direction.Left => Direction.Up,
        Direction.Right => Direction.Down,
        _ => dir,
      };
    }

    static (int, int) FindStartPosition(char[,] maze)
    {
      for (int row = 0; row < maze.GetLength(0); row++)
      {
        for (int col = 0; col < maze.GetLength(1); col++)
        {
          if (maze[row, col] == '^') return (row, col);
        }
      }
      return (0, 0);
    }
  }
}
