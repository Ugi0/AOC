#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

unordered_map<int, vector<pair<string, int>>> boxes;

int main() {
    string input;
    ifstream file;

    file.open("../input");
    if (!file.is_open()) {
        cerr << "Error: Could not open file" << endl;
        return 1;
    }

    long long ans1 = 0;
    long long ans2 = 0;

    while (getline(file, input)) {
        input += ",";
        string label;
        bool counting = true;
        long res1 = 0;
        long res2 = 0;
        for (size_t i = 0; i < input.size(); i++) {
            vector<pair<string, int>>::iterator it;
            switch (input[i]) {
                case ',':
                    ans1 += res1;
                    label.clear();
                    res1 = 0;
                    res2 = 0;
                    counting = true;
                    break;

                case '-':
                    it = find_if(boxes[res2].begin(), boxes[res2].end(),
                        [&label](const pair<string, int>& p) { return p.first == label; });
                    if (it != boxes[res2].end()) {
                        boxes[res2].erase(it);
                    }
                    break;
                case '=':
                    it = find_if(boxes[res2].begin(), boxes[res2].end(),
                        [&label](const pair<string, int>& p) { return p.first == label; });
                    if (it != boxes[res2].end()) {
                        *it = {label, input[i+1] - '0'};
                    } else {
                        boxes[res2].push_back(pair<string, int>{label, input[i+1] - '0'});
                    }
                    counting = false;
                    break;
                default:
                    break;
            }

            if (input[i] != ',' && input[i] != '\n') { 
                res1 += int(input[i]);
                res1 *= 17;
                res1 %= 256;
                if (counting) {
                    res2 += int(input[i]);
                    res2 *= 17;
                    res2 %= 256;
                    label += input[i];
                }
            }
        }
    }

    for (const auto& x : boxes) {
        int count = 1;
        for (const auto& y : x.second) {
            ans2 += (x.first+1) * count * y.second;
            count++;
        }
    }

    cout << "Part 1: " << ans1 << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}