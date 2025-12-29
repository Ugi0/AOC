#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string input;
    ifstream file;
    int ans = 0;
    int ans2 = 0;

    int colorMaxNumbers[] = {14, 13, 12};
    string colors[3] = {"blue", "green", "red"};

    file.open("../input");

    while (getline(file, input)) {
        int requiredCubes[3] = {0,0,0};
        bool valid = true;
        input += ";";
        int index = input.find(":") + 1;
        int gameNum = stoi(input.substr(4, index - 5));
        while (input.substr(index, input.size()).find(";") != std::string::npos) {
            int index2 = input.substr(index, input.size()).find(";");
            string roundString = input.substr(index, index2);
            roundString += ",";

            int i = 0;
            while (roundString.substr(i, roundString.size()).find(",") != std::string::npos) {
                int index3 = roundString.substr(i, roundString.size()).find(",");

                string colorString = roundString.substr(i + 1, index3 - 1);

                int j = colorString.find(" ");
                string color = colorString.substr(j + 1, colorString.size()-1);
                int number = stoi(colorString.substr(0, j));

                auto ptr = find(colors, colors + 3, color);

                int l = ptr - colors;
                if (number > colorMaxNumbers[l]) {
                    valid = false;
                }
                if (number > requiredCubes[l]) {
                    requiredCubes[l] = number;
                }
                
                i += index3 + 1;
            }

            index += index2 + 1;
        }
        ans2 += requiredCubes[0] * requiredCubes[1] * requiredCubes[2];
        if (valid) {
            ans += gameNum;
        }
    }
    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;
    return 0;
}