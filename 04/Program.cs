using System.Text.RegularExpressions;
namespace AdventOfCode
{
    class Day4 {

        static Dictionary<int, int> cards = new Dictionary<int, int>();
        static void Main(string[] args)
        {
            String? line;
            int totalPoints = 0;
            /* try */
            /* { */
            var test = new System.Diagnostics.Stopwatch();
            test.Start();
                StreamReader sr = new StreamReader("input.txt");
                line = sr.ReadLine();
                while (line != null) 
                {
                    int linePoints = ParseLine(line);
                    totalPoints += linePoints;
                    line = sr.ReadLine();
                }
                
                sr.Close();
                test.Stop();
            /* } */
            /* catch (Exception) */
            /* {} */
            int allCards = cards.Aggregate(0, (sum, kvPair) => sum + kvPair.Value);
            System.Console.WriteLine($"Part 1: {totalPoints}");
            System.Console.WriteLine($"Part 2: {allCards}");
            System.Console.WriteLine($"Time: {test.ElapsedMilliseconds} ms");
        }

        static int ParseLine(string line)
        {
            string rgStr = @"^Card +([0-9]+): *(([0-9]+ *)+) \| *(([0-9]+ *)+)$";
            Regex rg = new Regex(rgStr);
            Match match = rg.Match(line);
            if (!match.Success) return 0;

            HashSet<string> winningNums = Regex.Split(match.Groups[2].Value, @"\s+").ToHashSet();
            string[] myNums = Regex.Split(match.Groups[4].Value, @"\s+");
            int matches = 0;
            int cardPoints = myNums.Aggregate(0, 
                (points, current) => 
                {
                    if (!winningNums.Contains(current)) return points;
                    matches++;
                    return points == 0 ? 1 : points * 2;
                }
            );
            int card = int.Parse(match.Groups[1].Value);
            if (!cards.ContainsKey(card)) cards.Add(card, 1);
            for (int i = card + 1; i <= card + matches; ++i)
            {
                if (!cards.ContainsKey(i)) cards.Add(i, 1);
                cards[i] += cards[card];
            }
            return cardPoints;             
        }
    }
}
