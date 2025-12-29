#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <unordered_map>
using namespace std;

namespace std {
    template <>
    struct hash<vector<int>> {
        size_t operator()(const vector<int>& v) const {
            size_t seed = 0;
            for (int i : v) {
                seed ^= hash<int>{}(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
            }
            return seed;
        }
    };
}

struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const {
        size_t hash1 = hash<T1>{}(p.first);
        size_t hash2 = hash<T2>{}(p.second);
        return hash1
               ^ (hash2 + 0x9e3779b9 + (hash1 << 6)
                  + (hash1 >> 2));
    }
};

unordered_map<pair<string, vector<int>>, long long, hash_pair> mem;
int ans = 0;
unsigned long long ans2 = 0;

long long recur(string input, vector<int> goal) {
    if (mem.find(pair{input, goal}) != mem.end()) return mem[pair{input, goal}];
    if (input.size() == 0) {
        if (goal.size() == 0) return 1;
        return 0;
    }
    if (input[0] == '.') {
        input.erase(0, 1);
        return recur(input, goal);
    } else if (input[0] == '#') {
        if (goal.size() == 0) return 0;
        for (int i = 0; i < goal.at(0); i++) {
            if (input[i] != '#' && input[i] != '?') return 0;
        }
        if (input.size() != static_cast<std::string::size_type>(goal.at(0)) && (input[goal.at(0)] != '.' && input[goal.at(0)] != '?')) return 0;
        input.erase(0, goal.at(0)+1);
        goal.erase(goal.begin());
        return recur(input, goal);
    } else {
        string input1 = input;
        string input2 = input;
        input1[0] = '.';
        input2[0] = '#';
        long long temp = recur(input1, goal) + recur(input2, goal);
        mem[pair{input, goal}] = temp;
        return temp;
    }
}

int main() {
    string input;
    ifstream file;

    file.open("../input");

    while (getline(file, input)) {
        int index = input.find(" ");
        std::string segment;
        vector<int> goal;
        vector<int> goal2;
        std::stringstream ss(input.substr(index, input.size()));
        while(std::getline(ss, segment, ',')) {
            goal.push_back(stoi(segment));
        }
        ans += recur(input.substr(0, index), goal);
        string input2;
        for (int i = 0; i < 5; i++) {
            for (auto const& x : goal) goal2.push_back(x);
            input2 += input.substr(0, index);
            if (i != 4) input2 += '?';
        }
        ans2 += recur(input2, goal2);
        mem.clear();
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}