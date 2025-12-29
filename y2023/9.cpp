#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string input;
    ifstream file;

    file.open("../input");

    long ans = 0;
    long ans2 = 0;

    while (getline(file, input)) {
        vector<vector<long>> arr = {
            vector<long>()
        };
        int temp = 0;
        int temp2 = 0;
        int index = 0;
        input += " ";
        while (input.substr(index, input.size()).find(" ") != string::npos) {
            int index2 = input.substr(index, input.size()).find(" ");
            arr[0].push_back(stol(input.substr(index, index2)));
            index += index2 + 1;
        }
        int j = 0;
        while (true) {
            bool done = true;
            for (const long& x : arr[j]) {
                if (x != 0) done = false;
            }
            if (arr[j].size() == 0) break;
            if (done) break;
            arr.push_back(vector<long>());
            for (size_t k = 0; k < arr[j].size() - 1; k++) {
                arr[j+1].push_back(arr[j][k+1] - arr[j][k]);
            }
            j++;
        }
        int lastValue = 0;
        for (; j >= 0; j--) {
            temp += arr[j][arr[j].size()-1];
            if (j != 0) {
                lastValue = arr[j - 1][0] - lastValue;
                temp2 = lastValue;
            }
        }
        ans += temp;
        ans2 += temp2;
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}