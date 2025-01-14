#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> map;
vector<int> horizontal;
vector<int> vertical;
long ans;

bool verify(int index) {
    vector<string> map2;
    for (int i = 0; i < map.at(0).size(); i++) {
        map2.push_back("");
        for (auto const& x : map) {
            map2[i] += x[i];
        }        
    }
    int j = 0;
    bool found = true;
    while (index - 1 - j >= 0 && index + j < map2.size()) {
        if (map2[index - 1 - j] != map2[index + j]) found = false;
        j++;
    }
    return found;
}

void solve() {
    for (const auto& x : map) {
        int count = 0;
        for (const auto& y : x) {
            if (y == '#') count++; 
        }
        horizontal.push_back(count);
    }
    for (int i = 0; i < map.at(0).size(); i++) {
        int count = 0;
        for (auto const& x : map) {
            if (x[i] == '#') count++;
        }
        vertical.push_back(count);
    }
    for (int i = 1; i < horizontal.size(); i++) {
        bool found = true;
        int j = 0;
        while (i - 1 - j >= 0 && i + j < horizontal.size()) {
            if (horizontal[i + j] != horizontal[i - 1 - j] || map[i+j] != map[i-1-j]) {
                found = false;
                break;
            }
            j++;
        }
        if (found) {
            ans += 100*i;
            //cout << "Found horizontal: " << i << endl;
        }
    }
    for (int i = 1; i < vertical.size(); i++) {
        bool found = true;
        int j = 0;
        while (i - 1 - j >= 0 && i + j < vertical.size()) {
            if (vertical[i + j] != vertical[i - 1 - j]) {
                found = false;
                break;
            }
            j++;
        }
        if (found && verify(i)) {
            ans += i;
            //cout << "Found vertical: " << i << endl;
        }
    }
    vertical.clear();
    horizontal.clear();
    map.clear();
}

int main() {
    string input;
    ifstream file;

    file.open("../input");

    while (getline(file, input)) {
        if (input.size() != 0) { map.push_back(input); continue; }
        solve();
    }
    solve();

    cout << "Part 1: " << ans << endl;

    return 0;
}