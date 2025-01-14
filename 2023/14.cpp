#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

vector<string> map;
long ans;

int main() {
    string input;
    ifstream file;

    file.open("../input");

    int i = 0;
    while (getline(file, input)) {
        map.push_back(input);
        i++;
    }

    for (size_t i = 1; i < map.size(); i++) {
        for (size_t j = 0; j < map[0].size(); j++) {
            if (map[i][j] == 'O') {
                if ((i == 0) || (map[i-1][j] != '.')) continue;
                int k = 0;
                do {
                    k++;
                } while (i - k > 0 && map[i-k-1][j] == '.');
                map[i][j] = '.';
                map[i-k][j] = 'O';
            }
        }
    }

    for (size_t i = 0; i < map.size(); i++) {
        for (size_t j = 0; j < map[0].size(); j++) {
            if (map[i][j] == 'O') {
                ans += map.size() - i;
            }
        }
    }

    cout << "Part 1: " << ans << endl;

    return 0;
}