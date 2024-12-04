import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        int runningSum1 = 0;
        int runningSum2 = 0;
        Scanner scanner = parseInput("input.txt");
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] lineSplit = line.split(": ");
            int id = parseGameID(lineSplit[0]);
            if (isGamePossible(lineSplit[1])) {
                runningSum1 += id;
            }
            runningSum2 += minGameBallsPower(lineSplit[1]);

        }
        System.out.println("Part 1: " + runningSum1);
        System.out.println("Part 2: " + runningSum2);
    }

    static Scanner parseInput(String fileName) {
        try {
            File inputFile = new File(fileName);
            return new Scanner(inputFile);
        } catch (FileNotFoundException e) {
            return null;
        }
    }

    static int parseGameID(String line) {
        String pattern = "Game ([0-9]+)";
        Pattern p = Pattern.compile(pattern);
        Matcher m = p.matcher(line);
        m.find();
        return Integer.parseInt(m.group(1));
    }

    static int[] parseRound(String round) {
        int[] result = new int[3];
        String[] balls = round.split(", ");
        for (String color : balls) {
            String[] colorSplit = color.split(" ");
            switch(colorSplit[1]) {
                case "red":
                    result[0] = Integer.parseInt(colorSplit[0]);
                    break;
                case "green":
                    result[1] = Integer.parseInt(colorSplit[0]);
                    break;
                case "blue":
                    result[2] = Integer.parseInt(colorSplit[0]);
                    break;
            }
        }
        return result;
    }   

    static boolean isRoundPossible(int[] round) {
        return ((round[0] <= 12) && (round[1] <= 13) && (round[2] <=14));
    }

    static boolean isGamePossible(String gameRounds) {
        String[] rounds = gameRounds.split("; ");
        for (String round : rounds) {
            int[] roundParsed = parseRound(round);
            if (!isRoundPossible(roundParsed)) {
                return false;
            }
        }
        return true;
    }

    static int minGameBallsPower(String gameRounds) {
        int[] result = new int[3];
        String[] rounds = gameRounds.split("; ");
        for (String round : rounds) {
            int[] roundParsed = parseRound(round);
            result[0] = Math.max(result[0], roundParsed[0]);
            result[1] = Math.max(result[1], roundParsed[1]);
            result[2] = Math.max(result[2], roundParsed[2]);
        }
        return result[0] * result[1] * result[2];
    }
}