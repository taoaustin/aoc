using System.Collections.Immutable;

namespace AdventOfCode2024
{
  class Day2
  {
    public static (int, int) Solve()
    {
      string[] file = File.ReadAllLines("02/input.txt");
      int safe = 0;
      int safeDamp = 0;
      foreach (string line in file)
      {

        var nums = line.Split().Select(int.Parse).ToList();


        if (IsValid([.. nums]))
        {
          safe++;
        }
        if (IsValid([.. nums], true))
        {
          safeDamp++;
        }
      }
      return (safe, safeDamp);
    }

    static bool IsValid(ImmutableList<int> nums, bool dampen = false)
    {
      return IsIncreasing([.. nums], dampen) || IsDecreasing([.. nums], dampen);
    }


    static bool IsIncreasing(ImmutableList<int> nums, bool dampen = false)
    {
      for (int i = 0; i < nums.Count - 1; i++)
      {
        if ((nums[i] >= nums[i + 1]) || (Math.Abs(nums[i] - nums[i + 1]) > 3))
        {
          if (dampen)
          {
            return IsValid(nums.RemoveAt(i), false) || IsValid(nums.RemoveAt(i + 1), false);
          }
          else
          {
            return false;
          }
        }
      }
      return true;
    }

    static bool IsDecreasing(ImmutableList<int> nums, bool dampen = false)
    {
      for (int i = 0; i < nums.Count - 1; i++)
      {
        if ((nums[i] <= nums[i + 1]) || (Math.Abs(nums[i] - nums[i + 1]) > 3))
        {
          if (dampen)
          {
            return IsValid(nums.RemoveAt(i), false) || IsValid(nums.RemoveAt(i + 1), false);
          }
          else
          {
            return false;
          }
        }
      }
      return true;
    }
  }
}
