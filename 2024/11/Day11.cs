namespace AdventOfCode2024
{
  class Day11
  {
    public static (long, long) Solve()
    {
      var stones = Utils.ReadFileString(11, false).Split(null).Where(item => item != "").ToList();
      var p1 = stones;
      for (int i = 0; i < 25; i++)
      {
        p1 = Blink(p1);
      }
      Dictionary<string, long> stoneOccurences = stones.GroupBy(stone => stone).ToDictionary(group => group.Key, group => (long)group.Count());
      for (int i = 0; i < 75; i++)
      {
        stoneOccurences = Blink2(stoneOccurences);
      }
      long p2 = 0;
      foreach (var (k, v) in stoneOccurences)
      {
        p2 += v;
      }
      return (p1.Count, p2);
    }

    static List<string> Blink(List<string> stones)
    {
      var res = new List<string>();
      foreach (var stone in stones)
      {
        if (stone == "0")
        {
          res.Add("1");
        }
        else if (stone.Length % 2 == 0)
        {
          res.Add(long.Parse(stone[0..(stone.Length / 2)]).ToString());
          res.Add(long.Parse(stone[(stone.Length / 2)..]).ToString());
        }
        else
        {
          res.Add((long.Parse(stone) * 2024).ToString());
        }
      }
      return res;
    }

    // p2 filtered me, couldnt figure out just store the number of duplicates
    static Dictionary<string, long> Blink2(Dictionary<string, long> stones)
    {
      var res = new Dictionary<string, long>();
      foreach (var (stone, repeats) in stones)
      {
        var newStones = new List<string>();
        if (stone == "0")
        {
          newStones.Add("1");
        }
        else if (stone.Length % 2 == 0)
        {
          newStones.Add(long.Parse(stone[0..(stone.Length / 2)]).ToString());
          newStones.Add(long.Parse(stone[(stone.Length / 2)..]).ToString());
        }
        else
        {
          newStones.Add((long.Parse(stone) * 2024).ToString());
        }

        foreach (var newStone in newStones)
        {
          res.TryGetValue(newStone, out long val);
          res[newStone] = val + repeats;
        }
      }
      return res;
    }
  }
}
