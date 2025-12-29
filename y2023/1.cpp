#include <fstream>
#include <iostream>
#include <string>
using namespace std;

string ReplaceWithNumbers(string str);

int main() {

  string input;
  ifstream file;

  int first, first2;
  int last, last2;
  int count, count2;

  int ans, ans2 = 0;
    
  file.open("../input");

  size_t nums[9] = {1,2,3,4,5,6,7,8,9};
  string numbers[9] = {
      "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
  };
  
  while (getline(file, input)) {
    first = 0, first2 = 0;
    last = 0, last2 = 0;
    count = 0, count2 = 0;
    size_t size = input.length();
    for (size_t i = 0; i < size ; i++) {
      int number = input.at(i) - '0';
      if (number > 0 && number < 10) {
        count++;
        count2++;
        if (first == 0) {
          first = number;
        } else {
          last = number;
        }
        if (first2 == 0) {
          first2 = number;
        } else {
          last2 = number;
        }
      } else {
        for (int j = 0; j < 9; j++) {
          if (input.find(numbers[j], i) == i) {
            count2++;
            if (first == 0) {
              first2 = nums[j];
            } else {
              last2 = nums[j];
            }
          }
        }
      }
    }
    if (count > 0) {
      if (count == 1) {
        ans += 10*first + first;
      } else {
        ans += 10*first + last;
      }
    }
    if (count2 > 0) {
      if (count2 == 1) {
        ans2 += 10*first2 + first2;
      } else {
        ans2 += 10*first2 + last2;
      }
    }
  }
  cout << "Part 1: " << ans << endl;
  cout << "Part 2: " << ans2 << endl;

  return 0;
}