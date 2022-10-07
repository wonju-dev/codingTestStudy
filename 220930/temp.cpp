#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int testCase, length;
    cin >> testCase;
    while (testCase--) {
        cin >> length;
        vector<string> opStack;
        vector<long long> numStack;
        string temp;
        while (length-- > 0) {
            cin >> temp;
            if (temp == ")") {
                
                long long bNum = numStack.back();
                numStack.pop_back();

                string bCal = opStack.back();
                opStack.pop_back();

                long long rBrace = bNum;

                while (bCal != "(") {
                    bNum = numStack.back();
                    numStack.pop_back();

                    rBrace += bNum;
                    
                    bCal = opStack.back();
                    opStack.pop_back();
                }

                if (!(opStack.empty())) {
                    if (opStack.back() == "*") {
                        opStack.pop_back();
                        long long front_brace_num = numStack.back();
                        numStack.pop_back();
                        rBrace *= front_brace_num;
                    }
                    else if (opStack.back() == "-") {
                        opStack.pop_back();
                        opStack.push_back("+");
                        rBrace *= (-1);
                    }
                }
                numStack.push_back(rBrace);
                continue;
            }
            if (temp == "*") {
                cin >> temp;
                length--;
                if (temp == "(") {
                    opStack.push_back("*");
                    opStack.push_back("(");
                }
                else {
                    long long front_num = numStack.back();
                    numStack.pop_back();
                    long long mul_result = front_num * stoi(temp);
                    numStack.push_back(mul_result);
                }
                continue;
            }
            if (temp == "-") {
                cin >> temp;
                length--;
                if (temp == "(") {
                    opStack.push_back("-");
                    opStack.push_back("(");
                }
                else {
                    opStack.push_back("+");
                    long long num_temp = stoi(temp) * (-1);
                    numStack.push_back(num_temp);
                }
                continue;
            }
            if ((temp == "+") || (temp == "(")) {
                opStack.push_back(temp);
                continue;
            }

            numStack.push_back(stoi(temp));
        }

        long long result = numStack.back();
        numStack.pop_back();

        if (!numStack.empty()) {
            while (!numStack.empty()) {
                result += numStack.back();
                numStack.pop_back();
            }
        }

        cout << result << "\n";
    }
}