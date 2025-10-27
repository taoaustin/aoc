namespace AdventOfCode2024
{
  class Day7
  {
    enum Operation
    {
      Multiply,
      Add,
      Concat
    }
    public static (long, long) Solve()
    {
      string[] lines = Utils.ReadFileLines(7, false);
      Operation[] opList = [Operation.Multiply, Operation.Add];
      long part1 = 0;
      long part2 = 0;
      foreach (var item in lines)
      {
        var (result, operands) = ParseLineValues(item);
        var opCombinations = GetPermutationsWithRept(opList, operands.Length - 1);
        foreach (var opComb in opCombinations)
        {
          var ok = Calculate(result, new Stack<long>(operands.Reverse()), new Stack<Operation>(opComb));
          if (ok)
          {
            part1 += result;
            break;
          }
        }
        opList = [.. opList, Operation.Concat];
        opCombinations = GetPermutationsWithRept(opList, operands.Length - 1);
        foreach (var opComb in opCombinations)
        {
          var ok = Calculate(result, new Stack<long>(operands.Reverse()), new Stack<Operation>(opComb));
          if (ok)
          {
            part2 += result;
            break;
          }
        }
      }

      return (part1, part2);
    }

    static (long, long[]) ParseLineValues(string line)
    {
      string[] parts = line.Split(":");
      var result = parts[0];
      var parsedResult = long.Parse(result);
      var operands = parts[1].Split(" ").Where(item => item != "");
      long[] parsedOperands = [.. operands.Select(long.Parse)];
      return (parsedResult, parsedOperands);
    }


    static bool Calculate(long result, Stack<long> operands, Stack<Operation> ops)
    {
      if (operands.Count != ops.Count + 1)
      {
        throw new Exception("unexpected count");
      }
      var acc = operands.Pop();
      while (operands.Count > 0)
      {
        var next = operands.Pop();
        var nextOp = ops.Pop();
        switch (nextOp)
        {
          case Operation.Multiply:
            acc *= next;
            break;
          case Operation.Add:
            acc += next;
            break;
          case Operation.Concat:
            acc = long.Parse($"{acc}{next}");
            break;
        }
      }
      return acc == result;
    }


    static IEnumerable<IEnumerable<T>> GetPermutationsWithRept<T>(IEnumerable<T> list, int length)
    {
      if (length == 1) return list.Select(t => new T[] { t });
      return GetPermutationsWithRept(list, length - 1).
        SelectMany(t => list, (t1, t2) => t1.Concat([t2]));
    }
  }
}
