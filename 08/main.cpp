#include <numeric>
#include <string>
#include <fstream>
#include <iostream>
#include <regex>
#include <vector>
#include <unordered_map>
#include <utility>

using namespace std;

int main() {
    unordered_map<string, pair<string, string>> map;
    ifstream file ("input.txt");
    string cur_line;
    string instructions;
    regex rgx ("([A-Z]+) = \\(([A-Z]+), ([A-Z]+)\\)");
    smatch matches;
    getline(file, instructions);
    vector<string> start_nodes;
    while(getline(file, cur_line)) {
        if (regex_search(cur_line, matches, rgx)) {
            map[matches[1].str()] = make_pair(matches[2].str(), matches[3].str());
            if (matches[1].str().back() == 'A') {
                start_nodes.push_back(matches[1].str());
            }
        }
    }
    int steps = 0;
    string node = "AAA";
    int silver = 0;
    int i = 0;
    while (node != "ZZZ") {
        node = (instructions[i] == 'L') ? map[node].first : map[node].second;
        i = (i + 1) % instructions.size();
        silver++;
    }
    cout << "Part 1: " << silver << endl;
    vector<int> cycles;
    for (int i = 0; i < start_nodes.size(); ++i) {
        string node = start_nodes[i];
        int counter = 0;
        int j = 0;
        while (node.back() != 'Z') {
            node = (instructions[j] == 'L') ? map[node].first : map[node].second;
            j = (j + 1) % instructions.size();
            counter++;
        }
        cycles.push_back(counter);
    }
    long gold = 1; // wrong answer cause using int instead of long 
    for (int i = 0; i < cycles.size(); ++i) {
        gold = lcm(gold, cycles[i]);
    }
    cout << "Part 2: " << gold << endl;
}

// gold: some magic lcm solution :/. A general solution needs like chinese remainder theorem, cycle detection... or something?


