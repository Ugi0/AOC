#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
#include <unordered_map>
using namespace std;

string cardStrength = "23456789TJQKA";
string cardStrength2 = "J23456789TQKA";

bool compare_nums(int a, int b) {
    return a > b;
}

bool compare_hands(tuple<string, int> a, tuple<string, int> b) {
    for (int i = 0; i < 5; i++) {
        if (!(cardStrength.find(get<0>(a).at(i)) == cardStrength.find(get<0>(b).at(i)))) {
            if (cardStrength.find(get<0>(a).at(i)) < cardStrength.find(get<0>(b).at(i))) {
                return false;
            } 
            return true;
        }
    }
    return true;
}

bool compare_hands2(tuple<string, int> a, tuple<string, int> b) {
    for (int i = 0; i < 5; i++) {
        if (!(cardStrength2.find(get<0>(a).at(i)) == cardStrength2.find(get<0>(b).at(i)))) {
            if (cardStrength2.find(get<0>(a).at(i)) < cardStrength2.find(get<0>(b).at(i))) {
                return false;
            } 
            return true;
        }
    }
    return true;
}

int main() {
    string input;
    ifstream file;

    int ans = 0;
    int ans2 = 0;

    file.open("../input");

    vector<tuple<string, int>> hands;
    vector<vector<tuple<string, int>>> handTypes = {
        vector<tuple<string, int>>(), vector<tuple<string, int>>(), vector<tuple<string, int>>(),vector<tuple<string, int>>(),
        vector<tuple<string, int>>(), vector<tuple<string, int>>(), vector<tuple<string, int>>()
    };
    vector<vector<tuple<string, int>>> handTypes2 = {
        vector<tuple<string, int>>(), vector<tuple<string, int>>(), vector<tuple<string, int>>(),vector<tuple<string, int>>(),
        vector<tuple<string, int>>(), vector<tuple<string, int>>(), vector<tuple<string, int>>()
    };

    while (getline(file, input)) {
        hands.push_back(make_tuple(input.substr(0, 5), stoi(input.substr(6))));
    }

    for (size_t i = 0; i < hands.size(); i++) {
        unordered_map<char, int> cardType;
        unordered_map<char, int> cardType2;
        vector<int> values;
        vector<int> values2;
        int jokers = 0;
        for (string::size_type j = 0; j < get<0>(hands.at(i)).size(); j++) {
            cardType[get<0>(hands.at(i)).at(j)]++;
            if (get<0>(hands.at(i)).at(j) == 'J') {
                jokers++;
            } else {
                cardType2[get<0>(hands.at(i)).at(j)]++;
            }
        }
        for (auto const& x : cardType) {
            values.push_back(x.second);
        }
        for (auto const& x : cardType2) {
            values2.push_back(x.second);
        }
        sort(values.begin(), values.end(), compare_nums);
        sort(values2.begin(), values2.end(), compare_nums);
        if (values2.size() == 0) {
            values2.push_back(0);
        }
        values2[0] += jokers;
        if (values.size() == 1) {
            handTypes.at(0).push_back(hands.at(i));
        } else if (values.size() == 2 && values.at(0) == 4) {
            handTypes.at(1).push_back(hands.at(i));
        } else if (values.size() == 2 && values.at(0) == 3) {
            handTypes.at(2).push_back(hands.at(i));
        } else if (values.size() == 3 && values.at(0) == 3) {
            handTypes.at(3).push_back(hands.at(i));
        } else if (values.size() == 3 && values.at(0) == 2 && values.at(1) == 2) {
            handTypes.at(4).push_back(hands.at(i));
        } else if (values.size() == 4) {
            handTypes.at(5).push_back(hands.at(i));
        } else {
            handTypes.at(6).push_back(hands.at(i));
        }

        if (values2.size() == 1) {
            handTypes2.at(0).push_back(hands.at(i));
        } else if (values2.size() == 2 && values2.at(0) == 4) {
            handTypes2.at(1).push_back(hands.at(i));
        } else if (values2.size() == 2 && values2.at(0) == 3) {
            handTypes2.at(2).push_back(hands.at(i));
        } else if (values2.size() == 3 && values2.at(0) == 3) {
            handTypes2.at(3).push_back(hands.at(i));
        } else if (values2.size() == 3 && values2.at(0) == 2 && values2.at(1) == 2) {
            handTypes2.at(4).push_back(hands.at(i));
        } else if (values2.size() == 4) {
            handTypes2.at(5).push_back(hands.at(i));
        } else {
            handTypes2.at(6).push_back(hands.at(i));
        }
    }

    int count = 0;
    int count2 = 0;
    for (size_t i = 0; i < handTypes.size(); i++) {
        if (handTypes.at(i).size() != 0) {
            sort(handTypes.at(i).begin(), handTypes.at(i).end(), compare_hands);
        }
        if (handTypes2.at(i).size() != 0) {
            sort(handTypes2.at(i).begin(), handTypes2.at(i).end(), compare_hands2);
        }
        for (size_t j = 0; j < handTypes.at(i).size(); j++) {
            ans += get<1>(handTypes.at(i).at(j)) * (hands.size() - count);
            count++;
        }
        for (size_t j = 0; j < handTypes2.at(i).size(); j++) {
            ans2 += get<1>(handTypes2.at(i).at(j)) * (hands.size() - count2);
            count2++;
        }
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}