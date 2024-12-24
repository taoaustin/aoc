namespace AdventOfCode2024
{
    class Day1
    {
        public static (int, int) Solve()
        {
            string[] file = File.ReadAllLines("01/input.txt");
            int[] left = new int[file.Length];
            int[] right = new int[file.Length];
            for (int i = 0; i < file.Length; i++)
            {
                string[] line = file[i].Split(new char[0], StringSplitOptions.RemoveEmptyEntries);
                left[i] = Int32.Parse(line[0]);
                right[i] = Int32.Parse(line[1]);
            }
            int listDistance = distance(left, right);
            int listSimilarity = similarity(left, right);
            return (listDistance, listSimilarity);
        }

        static int distance(int[] left, int[] right)
        {
            Array.Sort(left);
            Array.Sort(right);
            int counter = 0;
            var pairs = left.Zip(right);
            foreach (var x in pairs)
            {
                counter += Math.Abs(x.First - x.Second);
            }
            return counter;
        }

        static int similarity(int[] left, int[] right)
        {
            Dictionary<int, int> occurenceMap = new Dictionary<int, int>();
            foreach (var id in right)
            {
                occurenceMap[id] = occurenceMap.TryGetValue(id, out var count) ? count + 1 : 1;
            }
            int similarity = 0;
            foreach (var id in left)
            {
                var occurences = occurenceMap.TryGetValue(id, out var count) ? count : 0;
                similarity += (occurences * id);
            }
            return similarity;
        }


    }
}
