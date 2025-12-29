#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string input;
    ifstream file;

    int ans = 1;
    int ans2 = 0;

    vector<int> times;
    vector<tuple<int, int>> races;

    file.open("../input");

    int line = 0;
    while (getline(file, input)) {
        input += " ";
        if (line == 0) {
            bool count = false;
            string temp = "";
            for (std::string::size_type i = 0; i < input.size(); i++) {
                if (input[i] == ':') {
                    count = true;
                    continue;
                }
                if (count) {
                    if (input[i] == ' ') {
                        if (temp.size() != 0) {
                            times.push_back(stoi(temp));
                            temp = "";
                        }
                    } else {
                        temp += input[i];
                    }
                }
            }
            line++;
        } else {
            bool count = false;
            string temp = "";
            for (std::string::size_type i = 0; i < input.size(); i++) {
                if (input[i] == ':') {
                    count = true;
                    continue;
                }
                if (count) {
                    if (input[i] == ' ') {
                        if (temp.size() != 0) {
                            races.push_back(make_tuple(times.at(races.size()), stoi(temp)));
                            temp = "";
                        }
                    } else {
                        temp += input[i];
                    }
                }
            }
        }
    }

    for (vector<tuple<int, int>>::size_type i = 0; i < races.size(); i++) {
        int count = 0;
        for (int charging = 0; charging <= get<0>(races.at(i)); charging++) {
            if ( (get<0>(races.at(i)) - charging) * charging > get<1>(races.at(i))) {
                count++;
            }
        }
        ans *= count;
    }

    string temp = "";
    for (vector<int>::size_type i = 0; i < times.size(); i++) {
        temp += to_string(times.at(i));
    }
    unsigned long long totalTime = stoull(temp);
    temp = "";
    for (vector<tuple<int, int>>::size_type i = 0; i < races.size(); i++) {
        temp += to_string(get<1>(races.at(i)));
    }
    unsigned long long totalDistance = stoull(temp);
    for (unsigned long long charging = 0; charging < totalTime; charging++) {
        if ( (totalTime - charging) * charging > totalDistance) {
            ans2++;
        }
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}