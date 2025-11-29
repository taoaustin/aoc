using System.Text.RegularExpressions;
using MathNet.Numerics.LinearAlgebra;

namespace AdventOfCode2024
{
  class Day13
  {
    public static (long, long) Solve()
    {
      string[] lines = Utils.ReadFileLines(13, false);

      Regex aPattern = new(@"Button A: X\+(\d+), Y\+(\d+)");
      Regex bPattern = new(@"Button B: X\+(\d+), Y\+(\d+)");
      Regex prizePattern = new(@"Prize: X=(\d+), Y=(\d+)");
      long part1 = 0;
      long part2 = 0;
      for (int i = 0; i <= lines.Length / 4; i++)
      {
        Match match = aPattern.Match(lines[i * 4 + 0]);
        var xIncrA = int.Parse(match.Groups[1].Value);
        var yIncrA = int.Parse(match.Groups[2].Value);
        (int, int) buttonA = (xIncrA, yIncrA);

        match = bPattern.Match(lines[i * 4 + 1]);
        var xIncrB = int.Parse(match.Groups[1].Value);
        var yIncrB = int.Parse(match.Groups[2].Value);
        (int, int) buttonB = (xIncrB, yIncrB);

        match = prizePattern.Match(lines[i * 4 + 2]);
        var xPrize = int.Parse(match.Groups[1].Value);
        var yPrize = int.Parse(match.Groups[2].Value);
        (long, long) prize = (xPrize, yPrize);
        // var res = MinTokens(buttonA, buttonB, prize);
        var res = MathSolution(buttonA, buttonB, prize);
        if (res > 0)
        {
          part1 += res;
        }
        var res2 = MathSolution(buttonA, buttonB, (xPrize + 10000000000000, yPrize + 10000000000000));
        if (res2 > 0)
        {
          part2 += res2;
        }

      }
      return (part1, part2);
    }

    static int MinTokens((int, int) buttonA, (int, int) buttonB, (int, int) prize)
    {
      var memo = new Dictionary<(int, int), int>();
      int Rec((int, int) rem)
      {
        if (memo.TryGetValue(rem, out int val))
        {
          return val;
        }
        else if (rem == (0, 0))
        {
          return 0;
        }
        else if (rem.Item1 < 0 || rem.Item2 < 0)
        {
          return -1;
        }
        var recA = Rec((rem.Item1 - buttonA.Item1, rem.Item2 - buttonA.Item2));
        var recB = Rec((rem.Item1 - buttonB.Item1, rem.Item2 - buttonB.Item2));
        int res = -1;
        if (recA >= 0)
        {
          res = 3 + recA;
        }
        if (recB >= 0 && (res == -1 || recB + 1 < res))
        {
          res = 1 + recB;
        }
        memo[rem] = res;
        return res;
      }
      return Rec(prize);
    }

    static long MathSolution((int, int) buttonA, (int, int) buttonB, (long, long) prize)
    {
      var A = Matrix<double>.Build.DenseOfArray(new double[,] {
          {buttonA.Item1, buttonB.Item1},
          {buttonA.Item2, buttonB.Item2},
          });
      var b = Vector<double>.Build.Dense([prize.Item1, prize.Item2]);
      var x = A.Solve(b);
      if (x == null)
      {
        return -1;
      }
      else if (Utils.IsAlmostEquals(x[0], (long)Math.Round(x[0]), 0.0001) && Utils.IsAlmostEquals(x[1], (long)Math.Round(x[1]), 0.0001))
      {
        return 3 * (long)Math.Round(x[0]) + (long)Math.Round(x[1]);
      }
      else
      {
        return -1;
      }
    }
  }
}
