#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string tmp;
    int testCase, n, m, d;
    cin >> testCase;
    
    while (testCase--) {
        cin >> n >> m >> d;
        
        int rowLen = n * 2 - 1, qRow = -1;
        string graph[m];                
        for (int i = m - 1; i >= 0; i--) {
            cin >> tmp;
            graph[i] = tmp;
            if (graph[i][0] == '?') {
                qRow = i;
            }
        }

        int current = 2 * d - 2;
        for (int i = 0; i < qRow; i++) {
            if ((1 < current) && (graph[i][current - 1] == '+')) {
                current -= 2; 
            }
            else if ((current < (rowLen - 2)) && (graph[i][current + 1] == '+')) {
                current += 2;
            }
        }

        vector<int> currents;
        currents.push_back(current); 
        if (1 < current) {
            currents.push_back(current - 2);
        }

        if (current < (rowLen - 2)) {
            currents.push_back(current + 2);
        }

        for (int i = qRow + 1; i < m; i++) {
            for (int j = 0; j < currents.size(); j++) {
                if ((1 < currents[j]) && (graph[i][currents[j] - 1] == '+')) {
                    currents[j] -= 2;
                }
                else if ((currents[j] < (rowLen - 2)) && (graph[i][currents[j] + 1] == '+')) {
                    currents[j] += 2;
                }
            }
        }

        sort(currents.begin(), currents.end());

        for (int i = 0; i < currents.size(); i++) {
            cout << (currents[i] + 2) / 2 << " ";
        }
        cout << endl;
    }
}