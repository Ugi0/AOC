#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

enum class state {
    SEEDS,
    SEEDTOSOIL,
    SOILTOFERTILIZER,
    FERTILIZERTOWATER,
    WATERTOLIGHT,
    LIGHTTOTEMPERATURE,
    TEMPERATURETOHUMIDITY,
    HUMIDITYTOLOCATION
};

int main() {
    string input;
    ifstream file;

    unsigned long int ans = ULONG_MAX;
    unsigned long int ans2 = ULONG_MAX;

    state currentState = state::SEEDS;

    file.open("../input");

    vector<unsigned long int> seeds;

    unordered_map<string, state> stateChanges = {
        {"seed-to-soil map:", state::SEEDTOSOIL},
        {"soil-to-fertilizer map:", state::SOILTOFERTILIZER},
        {"fertilizer-to-water map:", state::FERTILIZERTOWATER},
        {"water-to-light map:", state::WATERTOLIGHT},
        {"light-to-temperature map:", state::LIGHTTOTEMPERATURE},
        {"temperature-to-humidity map:", state::TEMPERATURETOHUMIDITY},
        {"humidity-to-location map:", state::HUMIDITYTOLOCATION}
    };

    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> seedToSoil;
    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> soilToFertilizer;
    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> fertilizerToWater;
    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> waterToLight;
    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> lightToTemperature;
    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> temperatureToHumidity;
    vector<tuple<unsigned long int, unsigned long int, unsigned long int>> humidityToLocation;

    unordered_map<state, unordered_map<unsigned long int ,bool>> stateCache = {
        {state::SOILTOFERTILIZER, unordered_map<unsigned long int, bool>()},
        {state::FERTILIZERTOWATER, unordered_map<unsigned long int, bool>()},
        {state::WATERTOLIGHT, unordered_map<unsigned long int, bool>()},
        {state::LIGHTTOTEMPERATURE, unordered_map<unsigned long int, bool>()},
        {state::TEMPERATURETOHUMIDITY, unordered_map<unsigned long int, bool>()},
        {state::HUMIDITYTOLOCATION, unordered_map<unsigned long int, bool>()}
    };

    unordered_map<state, vector<tuple<unsigned long int, unsigned long int, unsigned long int>>> stateToMap = {
        {state::SEEDTOSOIL, seedToSoil},
        {state::SOILTOFERTILIZER, soilToFertilizer},
        {state::FERTILIZERTOWATER, fertilizerToWater},
        {state::WATERTOLIGHT, waterToLight},
        {state::LIGHTTOTEMPERATURE, lightToTemperature},
        {state::TEMPERATURETOHUMIDITY, temperatureToHumidity},
        {state::HUMIDITYTOLOCATION, humidityToLocation}
    };

    while (getline(file, input)) {
        if (input.size() == 0) {
            continue;
        }
        bool changedState = false;
        for (auto const& x : stateChanges) {
            if (input.find(x.first) != string::npos) {
                currentState = x.second;
                changedState = true;
            }
        }
        if (changedState) continue;
        if (currentState == state::SEEDS) {
            int index = input.find(":") + 2;
            input += " ";
            while (input.substr(index, input.size()).find(" ") != string::npos) {
                int index2 = input.substr(index, input.size()).find(" ");
                seeds.push_back(stoul(input.substr(index, index2)));
                index += index2 + 1;
            }
        } else {
            int index = input.find(" ");
            unsigned long int first = stoul(input.substr(0, index));
            long index2 = input.substr(index + 1, input.size()).find(" ") + index;
            unsigned long int second = stoul(input.substr(index + 1, index2 - index ));
            unsigned long int third = stoul(input.substr(index2 + 2, input.size()));

            stateToMap[currentState].push_back(make_tuple(second, second+third-1, first));
        }
    }
    for (size_t j = 0; j < seeds.size() / 2; j++) {
        unsigned long int start = seeds[2 * j];
        unsigned long int length = seeds[2 * j + 1];
        cout << start << " " << length << endl;
        for (unsigned long int i = start; i <= start + length; i++) {
            unsigned long int currentSeed = i;
            unsigned long int currentSoil = ULONG_MAX;
            for (auto const& x : stateToMap[state::SEEDTOSOIL]) {
                if (currentSeed >= get<0>(x) && currentSeed <= get<1>(x)) {
                    currentSoil = (currentSeed - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentSoil == ULONG_MAX) {
                currentSoil = currentSeed;
            }
            if (stateCache[state::SOILTOFERTILIZER].find(currentSoil) != stateCache[state::SOILTOFERTILIZER].end()) {
                continue;
            }
            stateCache[state::SOILTOFERTILIZER][currentSoil] = true;
            unsigned long int currentFertilizer = ULONG_MAX;
            for (auto const& x : stateToMap[state::SOILTOFERTILIZER]) {
                if (currentSoil >= get<0>(x) && currentSoil <= get<1>(x)) {
                    currentFertilizer = (currentSoil - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentFertilizer == ULONG_MAX) {
                currentFertilizer = currentSoil;
            }
            if (stateCache[state::FERTILIZERTOWATER].find(currentFertilizer) != stateCache[state::FERTILIZERTOWATER].end()) {
                continue;
            }
            stateCache[state::FERTILIZERTOWATER][currentFertilizer] = true;
            unsigned long int currentWater = ULONG_MAX;
            for (auto const& x : stateToMap[state::FERTILIZERTOWATER]) {
                if (currentFertilizer >= get<0>(x) && currentFertilizer <= get<1>(x)) {
                    currentWater = (currentFertilizer - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentWater == ULONG_MAX) {
                currentWater = currentFertilizer;
            }
            unsigned long int currentLight = ULONG_MAX;
            for (auto const& x : stateToMap[state::WATERTOLIGHT]) {
                if (currentWater >= get<0>(x) && currentWater <= get<1>(x)) {
                    currentLight = (currentWater - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentLight == ULONG_MAX) {
                currentLight = currentWater;
            }
            if (stateCache[state::LIGHTTOTEMPERATURE].find(currentLight) != stateCache[state::LIGHTTOTEMPERATURE].end()) {
                continue;
            }
            stateCache[state::LIGHTTOTEMPERATURE][currentLight] = true;
            unsigned long int currentTemperature = ULONG_MAX;
            for (auto const& x : stateToMap[state::LIGHTTOTEMPERATURE]) {
                if (currentLight >= get<0>(x) && currentLight <= get<1>(x)) {
                    currentTemperature = (currentLight - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentTemperature == ULONG_MAX) {
                currentTemperature = currentLight;
            }
            if (stateCache[state::TEMPERATURETOHUMIDITY].find(currentTemperature) != stateCache[state::TEMPERATURETOHUMIDITY].end()) {
                continue;
            }
            stateCache[state::TEMPERATURETOHUMIDITY][currentTemperature] = true;
            unsigned long int currentHumidity = ULONG_MAX;
            for (auto const& x : stateToMap[state::TEMPERATURETOHUMIDITY]) {
                if (currentTemperature >= get<0>(x) && currentTemperature <= get<1>(x)) {
                    currentHumidity = (currentTemperature - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentHumidity == ULONG_MAX) {
                currentHumidity = currentTemperature;
            }
            if (stateCache[state::HUMIDITYTOLOCATION].find(currentHumidity) != stateCache[state::HUMIDITYTOLOCATION].end()) {
                continue;
            }
            stateCache[state::HUMIDITYTOLOCATION][currentHumidity] = true;
            unsigned long int currentLocation = ULONG_MAX;
            for (auto const& x : stateToMap[state::HUMIDITYTOLOCATION]) {
                if (currentHumidity >= get<0>(x) && currentHumidity <= get<1>(x)) {
                    currentLocation = (currentHumidity - get<0>(x)) + get<2>(x);
                    continue;
                }
            }
            if (currentLocation == ULONG_MAX) {
                currentLocation = currentHumidity;
            }
            //cout << currentSeed << " " << currentSoil << " " << currentFertilizer << " " << currentWater << " " << currentLight << " " << currentTemperature << " " << currentHumidity << " " << currentLocation << endl;
            if (ans > currentLocation && (i == start + length || i == start)) {
                ans = currentLocation;
            }
            if (ans2 > currentLocation) {
                ans2 = currentLocation;
            }
        }
    }

    cout << "Part 1: " << ans << endl;
    cout << "Part 2: " << ans2 << endl;

    return 0;
}