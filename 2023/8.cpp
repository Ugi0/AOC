#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <numeric>
using namespace std;

bool compareFunction (std::string a, std::string b) {return a<b;} 

unsigned long long gcd(unsigned long long a, unsigned long long b) {
    unsigned long long remainder = a % b;
    if (remainder == 0) return b;
    return gcd(b, remainder);
}

unsigned long long lcm(unsigned long long a, unsigned long long b) {
    return a * b / gcd(a, b);
}

int main() {
    string input;
    ifstream file;

    vector<string> startNodes;

    unsigned long long ans2 = 1;

    string path;
    unordered_map<string, pair<string, string>> map;
    vector<int> loopSizes;

    file.open("../input");

    unsigned long long i = 0;
    while (getline(file, input)) {
        if (i == 0) { path = input; i++; continue; }
        if (input == "") continue;

        int index = input.find("=");
        string key = input.substr(0, 3);

        string left = input.substr(index+3, 3);
        string right = input.substr(index+8, 3);

        map[key] = make_pair(left, right);
        i++;
    }

    for (auto const& x : map) {
        if (x.first.at(2) == 'A') {
            startNodes.push_back(x.first);
            loopSizes.push_back(0);
        }
    }

    sort(startNodes.begin(), startNodes.end(), compareFunction);
    i = 0;
    for (const string& x : startNodes) {
        string current = x;
        int j = 0;
        while (current.at(2) != 'Z') {
            loopSizes[i]++;
            if (path.at(j % path.size()) == 'L') {
                current = map[current].first;
            } else {
                current = map[current].second;
            }
            j++;
        }
        i++;
    }

    for (const int& x : loopSizes) {
        ans2 = lcm(ans2, x);
    }

    cout << "Part 1: " << loopSizes[0] << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}