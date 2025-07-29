namespace AdventOfCode2024
{
  class Day5
  {
    public static (int, int) Solve()
    {
      string[] file = Utils.ReadFileLines(5, false);
      var (rules, prints) = CreateRules(file);
      int validMids = 0, fixedMids = 0;
      foreach (string printing in prints)
      {
        List<string> printOrder = [.. printing.Split(",")];
        if (ApplyRules(printOrder, rules)) validMids += int.Parse(printOrder[printOrder.Count / 2]);
        else fixedMids += Fix(printOrder, rules);
      }
      return (validMids, fixedMids);
    }

    static int Fix(List<string> printOrder, Dictionary<string, List<string>> rules)
    {
      List<string> newOrder = [];
      for (int i = 0; i < printOrder.Count; i++)
      {
        var curRules = rules.GetValueOrDefault(key: printOrder[i], []);
        bool noInsert = true;
        for (int y = 0; y < newOrder.Count; y++)
        {
          if (curRules.Contains(newOrder[y]))
          {
            newOrder.Insert(y, printOrder[i]);
            noInsert = false;
            break;
          }
        }
        if (noInsert) newOrder.Add(printOrder[i]);
      }
      return int.Parse(newOrder[newOrder.Count / 2]);
    }

    static bool ApplyRules(List<string> printOrder, Dictionary<string, List<string>> rules)
    {
      for (int i = 1; i < printOrder.Count; i++)
      {
        var seenSoFar = printOrder[..i];
        var intersect = seenSoFar.Intersect(rules.GetValueOrDefault(key: printOrder[i], []));
        if (intersect.Any()) return false;
      }
      return true;
    }

    static (Dictionary<string, List<string>>, string[]) CreateRules(string[] rules)
    {
      Dictionary<string, List<string>> ruleMap = [];
      int i;
      for (i = 0; i < rules.Length; i++)
      {
        var rule = rules[i];
        if (rule.Equals("")) break;
        string[] parts = rule.Split(['|']);
        if (ruleMap.TryGetValue(parts[0], out List<string>? value)) value.Add(parts[1]);
        else ruleMap.Add(parts[0], [parts[1]]);
      }
      return (ruleMap, rules[(i + 1)..]);
    }
  }
}
