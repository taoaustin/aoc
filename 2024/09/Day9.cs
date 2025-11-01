namespace AdventOfCode2024
{
  class Day9
  {
    public static (long, long) Solve()
    {
      string disk = Utils.ReadFileString(9, false).Trim();
      var layout = DiskLayout(disk);
      var p1Layout = RearrangeLayout1([.. layout]);
      long checksum1 = CalculateChecksum(p1Layout);
      var p2Layout = RearrangeLayout2([.. layout]);
      long checksum2 = CalculateChecksum(p2Layout);
      return (checksum1, checksum2);
    }

    static int[] DiskLayout(string disk)
    {
      List<int> result = [];
      int id = 0;
      foreach (char c in disk)
      {
        var length = c - '0';
        if (id % 2 == 1)
        {
          result.AddRange(Enumerable.Repeat(-1, length));
        }
        else
        {
          result.AddRange(Enumerable.Repeat(id / 2, length));
        }
        id++;
      }
      return [.. result];
    }

    static int[] RearrangeLayout1(int[] layout) // 2 pointers!
    {
      int l = 0, r = layout.Length - 1;
      while (l < r)
      {
        if (layout[l] == -1 && layout[r] == -1)
        {
          r--;
        }
        else if (layout[l] == -1)
        {
          layout[l] = layout[r];
          layout[r] = -1;
          l++;
          r--;
        }
        else
        {
          l++;
        }
      }
      return layout;
    }

    static int[] RearrangeLayout2(int[] layout) // O(n^2) lazy
    {
      var finalID = Array.FindLast(layout, id => id != -1);
      for (int lastID = finalID; lastID >= 1; lastID--)
      {
        var lastIDIdx = Array.FindLastIndex(layout, id => id == lastID);
        var length = GetLengthOfIDBlock(layout, lastID, lastIDIdx);
        var freeBlockIdx = FindContiguousFreeBlock(layout, length);
        if (freeBlockIdx == -1 || freeBlockIdx > lastIDIdx)
        {
          continue;
        }
        Array.Copy(Enumerable.Repeat(lastID, length).ToArray(), 0, layout, freeBlockIdx, length);
        Array.Copy(Enumerable.Repeat(-1, length).ToArray(), 0, layout, lastIDIdx - length + 1, length);
      }
      return layout;
    }

    static int FindContiguousFreeBlock(int[] layout, int size)
    {
      int cur = 0;
      for (int i = 0; i < layout.Length; i++)
      {
        if (layout[i] == -1)
        {
          if (++cur == size)
          {
            return i - size + 1;
          }
        }
        else
        {
          cur = 0;
        }
      }
      return -1;
    }

    static int GetLengthOfIDBlock(int[] layout, int id, int startIdx)
    {
      var res = 0;
      while (layout[startIdx] == id)
      {
        res++;
        startIdx--;
      }
      return res;
    }

    static long CalculateChecksum(int[] layout)
    {
      long checksum = 0;
      for (int i = 0; i < layout.Length; i++)
      {
        if (layout[i] == -1)
        {
          continue;
        }
        checksum += i * layout[i];
      }
      return checksum;
    }
  }
}
