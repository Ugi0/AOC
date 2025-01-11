#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

pair<int, int> startPoint;
vector<vector<tuple<bool, bool, bool, bool>>> map;
vector<vector<int>> distances;
int ans = 0;

tuple<bool, bool, bool, bool> charToDirections(char c) {
    switch (c) {
    case '|':
        return tuple{true, false, true, false};
    case '-':
        return tuple{false, true, false, true};
    case 'L':
        return tuple{true, true, false, false};
    case 'J':
        return tuple{true, false, false, true};
    case '7':
        return tuple{false, false, true, true};
    case 'F':
        return tuple{false, true, true, false};
    case '.':
        return tuple{false, false, false, false};
    case 'S':
        return tuple{true, true, true, true};
    default:
        return tuple{false, false, false, false};
    }
}

void recur(int x, size_t y, int steps) {
    if (distances[x][y] == steps) { ans = steps; return; }
    if (distances[x][y] < steps) return;
    distances[x][y] = steps;
    if (y + 1 < map[x].size()) {
        if (get<1>(map[x][y]) && get<3>(map[x][y+1])) {
            recur(x, y+1, steps+1);
        }
    }
    if (y > 0) {
        if (get<3>(map[x][y]) && get<1>(map[x][y-1])) {
            recur(x, y-1, steps+1);
        }
    }
    if (x > 0) {
        if (get<0>(map[x][y]) && get<2>(map[x-1][y])) {
            recur(x-1, y, steps+1);
        }
    }
    if (x + 1 < static_cast<int>(map.size())) {
        if (get<2>(map[x][y]) && get<0>(map[x+1][y])) {
            recur(x+1, y, steps+1);
        }
    }
}


int main() {
    string input;
    ifstream file;

    file.open("../input");

    int i = 0;
    while (getline(file, input)) {
        map.push_back(vector<tuple<bool, bool, bool, bool>>());
        distances.push_back(vector<int>());
        for (size_t j = 0; j < input.size(); j++) {
            distances[i].push_back(INT_MAX);
            map[i].push_back(charToDirections(input[j]));
            if (input[j] == 'S') startPoint = pair{i, j};
        }
        i++;
    }

    recur(startPoint.first, startPoint.second, 0);

    /*for (const auto& a : distances) {
        for (const auto& b : a) {
            cout << b << " ";
        }
        cout << endl;
    }*/

    cout << "Part 1: " << ans << endl;

    return 0;
}