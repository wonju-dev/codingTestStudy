#include <iostream>
using namespace std;

int main()
{
    int loop;
    cin >> loop;
    while (loop--) {
        int length;
        cin >> length;
        int score = -1, graph[length + 1][5], dp[length + 1][5];
        
        for (int j = 0; j < 5; j++) {
            graph[0][j] = 1;
            dp[0][j] = -1;
        }
        

        int num = 0;
        for (int i = length; i >= 1; i--) {
            for (int j = 0; j < 5; j++) {
                cin >> num;
                graph[i][j] = num;
                dp[i][j] = -1;
            }
        }

        dp[length][2] = 0;
        dp[0][2] = 0;
        graph[0][2] = 0;

        for (int i = 1; i <= length; i++) { 
            for (int j = 0; j < 5; j++) {
                if (graph[i][j] != 1) {
                    dp[i][j] = graph[i][j];

                    if ((j > 0) && (graph[i][j - 1] == 1)) {
                        dp[i][j]++;
                    }
                    if ((j < 4) && (graph[i][j + 1] == 1)) {
                        dp[i][j]++;
                    }

                    int preMax = dp[i - 1][j];

                    if (j > 0) {
                        if (dp[i - 1][j - 1] > preMax) {
                            preMax = dp[i - 1][j - 1];
                        }
                    }

                    if (j < 4) {
                        if (dp[i - 1][j + 1] > preMax) {
                            preMax = dp[i - 1][j + 1];
                        }
                    }

                    dp[i][j] += preMax;
                }
            }
        }

        for (int i = 0; i < 5; i++) {
            if (score < dp[length][i]) {
                score = dp[length][i];
            }
        }

        cout << score << endl;
    }
}
