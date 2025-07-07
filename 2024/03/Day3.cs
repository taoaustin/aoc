using System.Text.RegularExpressions;

namespace AdventOfCode2024
{
  class Day3
  {
    public static (int, int) Solve()
    {
      string file = Utils.ReadFileString(3);
      string pattern = @"(mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\))";
      MatchCollection matches = Regex.Matches(file, pattern);
      int fullTally = 0;
      int filteredTally = 0;
      bool enabled = true;
      foreach (Match match in matches)
      {
        var groups = match.Groups;
        if (groups[0].Value == "do()") enabled = true;
        else if (groups[0].Value == "don't()") enabled = false;
        else if (enabled)
        {
          filteredTally += ParseMul(groups[2].Value, groups[3].Value);
          fullTally += ParseMul(groups[2].Value, groups[3].Value);
        }
        else fullTally += ParseMul(groups[2].Value, groups[3].Value);
      }
      return (fullTally, filteredTally);
    }

    static int ParseMul(string var1, string var2)
    {
      var val1 = int.Parse(var1);
      var val2 = int.Parse(var2);
      return val1 * val2;
    }
  }
}
