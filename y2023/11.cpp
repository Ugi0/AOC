#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <climits>
using namespace std;

vector<pair<int, int>> galaxies;
unordered_map<int, bool> verticalDoubles;
unordered_map<int, bool> horizontalDoubles;

unsigned long long ans = 0;

int main() {
    string input;
    ifstream file;

    file.open("../input");

    int i = 0;
    while (getline(file, input)) {
        for (size_t j = 0; j < input.size(); j++) {
            if (input.at(j) == '#') {
                galaxies.push_back(pair{i, j});
            }
        }
        i++;
    }

    for (int j = 0; j < i; j++) {
        bool doubled = true;
        for (auto& x : galaxies) {
            if (x.first == j) doubled = false;
        }
        if (doubled) horizontalDoubles[j] = true;
    }

    for (int j = 0; j < i; j++) {
        bool doubled = true;
        for (auto& x : galaxies) {
            if (x.second == static_cast<int>(j)) doubled = false;
        }
        if (doubled) verticalDoubles[j] = true;
    }

    for (const auto& x : galaxies) {
        for (const auto& y : galaxies) {
            for (int i = min(x.first, y.first); i < max(x.first, y.first); i++) {
                if (horizontalDoubles[i]) {
                    ans += 999999;
                }
            }
            for (int i = min(x.second, y.second); i < max(x.second, y.second); i++) {
                if (verticalDoubles[i]) {
                    ans += 999999;
                }
            }
            ans += max(x.second, y.second) - min(x.second, y.second);
            ans += max(x.first, y.first) - min(x.first, y.first);
        }
    }

    cout << ans/2 << endl;

    return 0;
}