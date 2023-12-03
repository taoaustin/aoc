import haxe.io.Eof;
import sys.io.FileInput;
import sys.io.File;

class Main {
    static public function main():Void {
        var totalSum = 0;
        var totalRatioSum = 0;
        var file:FileInput = File.read("input.txt");
        var curLine = file.readLine();
        var prevLine = "";
        for (i in 0...curLine.length) {
            prevLine += ".";
        }
        var nextLine = file.readLine();
        try {
            while (true) {
                totalSum += walkLines(prevLine, curLine, nextLine);
                totalRatioSum += walkLines2(prevLine, curLine, nextLine);
                prevLine = curLine;
                curLine = nextLine;
                nextLine = file.readLine();
            }
        } catch (e:Eof) {
            file.close();
            nextLine = "";
            for (i in 0...curLine.length) {
                nextLine += ".";
            }
            totalSum += walkLines(prevLine, curLine, nextLine);
            totalRatioSum += walkLines2(prevLine, curLine, nextLine);
        }
        trace("Part 1: " + totalSum);
        trace("Part 2: " + totalRatioSum);
    }

    static function walkLines(line0:String, line1:String, line2:String):Int {
        var r = ~/([0-9]+)/;
        var lineSum = 0;
        while (r.match(line1)) {
            var mPos = r.matchedPos();
            lineSum += checkAroundWord(line0, line1, line2, mPos.pos, mPos.len);
            line0 = line0.substr(mPos.pos + mPos.len);
            line1 = line1.substr(mPos.pos + mPos.len);
            line2 = line2.substr(mPos.pos + mPos.len);
        }
        return lineSum;
    }

    static function walkLines2(line0:String, line1:String, line2:String):Int {
        var lineRatiosSum = 0;
        for (i in 0...line1.length) {
            if (line1.charAt(i) == "*") {
                lineRatiosSum += checkGear(line0, line1, line2, i);
            }
        }
        return lineRatiosSum;
    }
    
    static function isSymbol(s:String):Bool {
        return (s != ".");
    }

    static function checkAroundWord(line0:String, line1:String, line2:String, pos:Int, len:Int):Int {
        var code = Std.parseInt(line1.substr(pos, len));
        for (i in pos...pos + len) {
            if (isSymbol(line0.charAt(i))) return code;
            if (isSymbol(line2.charAt(i))) return code;
        }
        
        if (pos > 0) {
            if (isSymbol(line0.charAt(pos - 1))) return code;
            if (isSymbol(line1.charAt(pos - 1))) return code;
            if (isSymbol(line2.charAt(pos - 1))) return code;
        }
        if (pos + len < line1.length) {
            if (isSymbol(line0.charAt(pos + len))) return code;
            if (isSymbol(line1.charAt(pos + len))) return code;
            if (isSymbol(line2.charAt(pos + len))) return code;
        }
        return 0;
    }

    static function checkGear(line0, line1, line2, i) {
        var line0Res = lineGears(line0, i);
        var line1Res = lineGears(line1, i);
        var line2Res = lineGears(line2, i);
        var gearTotal = line0Res[1] * line1Res[1] * line2Res[1];
        if (line0Res[0] + line1Res[0] + line2Res[0] != 2) {
            return 0;
        }
        return gearTotal;
    }

    static function lineGears(line, i) {
        var nums = 0;
        var total = 1;
        var forward = readForward(line, i + 1);
        if (forward != "") {
            nums++;
            total *= Std.parseInt(forward);
        }
        var back = readBackward(line, i - 1);
        if (back != "") {
            nums++;
            total *= Std.parseInt(back);
        }
        if (Std.parseInt(line.charAt(i)) != null) {
            nums = 1;
            total = Std.parseInt(back + line.charAt(i) + forward);
        }

        return [nums, total];

    }

    static function readForward(line, i) {
        var num = "";
        while (Std.parseInt(line.charAt(i)) != null) {
            num += line.charAt(i);
            i++;
        }
        return num;
    }

    static function readBackward(line, i) {
        var num = "";
        while (Std.parseInt(line.charAt(i)) != null) {
            num = line.charAt(i) + num;
            i--;
        }
        return num;
    }
}
