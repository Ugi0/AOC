#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    string input;
    ifstream file;

    int ans = 0;
    int ans2 = 0;

    file.open("../input");

    bool stopCounting = false;

    std::unordered_map<int, int> cardNumbers;
    for (int i = 0; i < 250; i++) {
        cardNumbers[i] = 1;
    }

    while (getline(file, input)) {
        int roundAns = 0;
        int roundNum = 0;
        int index = input.find(":") + 1;
        int gameNum = stoi(input.substr(4, index - 5));

        if (cardNumbers[gameNum - 1] == 0) {
            stopCounting = true;
        }

        int splitIndex = input.find("|");

        vector<int> correctArr;

        string correctString = input.substr(index, splitIndex -index);
        for (size_t i = 0; i < correctString.size() / 3; i++) {
            if (correctString[3*i + 1] == ' ') {
                correctArr.push_back(stoi(string(1, correctString[3*i + 2])));
            } else {
                correctArr.push_back(stoi(string(1, correctString[3*i + 1]) + string(1, correctString[3*i + 2])));           
            }
        }
        
        string testString = input.substr(splitIndex+1, input.size());
        for (size_t i = 0; i < testString.size() / 3; i++) {
            if (testString[3*i + 1] == ' ') {
                if (std::find(correctArr.begin(), correctArr.end(), stoi(string(1, testString[3*i + 2]))) != correctArr.end()) {
                    roundNum++;
                    cardNumbers[gameNum + roundNum] += cardNumbers[gameNum];
                    if (roundAns == 0) {
                        roundAns = 1;
                    } else {
                        roundAns *= 2;
                    }
                }
            } else {
                if (std::find(correctArr.begin(), correctArr.end(), stoi(string(1, testString[3*i + 1]) + string(1, testString[3*i + 2]))) != correctArr.end()) {
                    roundNum++;
                    cardNumbers[gameNum + roundNum] += cardNumbers[gameNum];
                    if (roundAns == 0) {
                        roundAns = 1;
                    } else {
                        roundAns *= 2;
                    }
                }
            }
        }
        ans += roundAns;
        if (!stopCounting) {
            ans2 += cardNumbers[gameNum];
        }
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}