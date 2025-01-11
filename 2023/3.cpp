#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

static string numbers = "1234567890";
static string chars = "1234567890.";
static bool cache[141][141];
static string matrix[141];

int constructNumber(int x, int y);
int checkAdjacent(int x, int y, int direction[2]);

int main() {
    string input;
    ifstream file;

    int ans = 0;
    int ans2 = 0;

    file.open("../input");
    static int adjacentTiles[8][2] = {{-1,0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};

    int i = 0;
    while (getline(file, input)) {
        matrix[i] = input;
        matrix[i] += ".";
        i++;
    }
    matrix[i] = std::string(input.size() + 1, '.');
    for (size_t i = 0; i < input.size(); i++) {
        for (size_t j = 0; j < input.size(); j++) {
            if (std::find(chars.begin(), chars.end(), matrix[i][j]) == chars.end()) {
                int num;
                vector<int> adjacentNumbers;
                if (i != 0 && j != 0) {
                    num = checkAdjacent(i, j, adjacentTiles[1]);
                    if (num != 0) adjacentNumbers.push_back(num);
                    ans += num;
                }
                if (i != 0) {
                    num = checkAdjacent(i, j, adjacentTiles[2]);
                    if (num != 0) adjacentNumbers.push_back(num);
                    ans += num;
                    num = checkAdjacent(i, j, adjacentTiles[3]);
                    if (num != 0) adjacentNumbers.push_back(num);
                    ans += num;
                }
                if (j != 0) {
                    num = checkAdjacent(i, j, adjacentTiles[0]);
                    if (num != 0) adjacentNumbers.push_back(num);
                    ans += num;
                    num = checkAdjacent(i, j, adjacentTiles[7]);
                    if (num != 0) adjacentNumbers.push_back(num);
                    ans += num;
                }
                num = checkAdjacent(i, j, adjacentTiles[4]);
                if (num != 0) adjacentNumbers.push_back(num);
                ans += num;
                num = checkAdjacent(i, j, adjacentTiles[5]);
                if (num != 0) adjacentNumbers.push_back(num);
                ans += num;
                num = checkAdjacent(i, j, adjacentTiles[6]);
                if (num != 0) adjacentNumbers.push_back(num);
                ans += num;

                if (adjacentNumbers.size() == 2) {
                    ans2 += adjacentNumbers[0] * adjacentNumbers[1];
                }
            }
        };
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}

int checkAdjacent(int x, int y, int direction[2]) {
    if ((std::find(numbers.begin(), numbers.end(), matrix[x+direction[0]][y+direction[1]]) != numbers.end())) {
        //this direction has a number
        if (cache[direction[0]][direction[1]]) return 0;

        return constructNumber(x+direction[0], y+direction[1]);
    }

    return 0;
}

int constructNumber(int x, int y) {
    string number(1, matrix[x][y]);
    cache[x][y] = true;
    //check left
    int i = 1;
    while ((std::find(numbers.begin(), numbers.end(), matrix[x][y - i]) != numbers.end())) {
        if (cache[x][y - i]) return 0;
        number = matrix[x][y - i] + number;
        cache[x][y - i] = true;
        i++;
    }
    //check right
    int j = 1;
    while ((std::find(numbers.begin(), numbers.end(), matrix[x][y + j]) != numbers.end())) {
        if (cache[x][y - i]) return 0;
        number = number + matrix[x][y + j];
        cache[x][y + j] = true;
        j++;
    }
    return stoi(number);
}