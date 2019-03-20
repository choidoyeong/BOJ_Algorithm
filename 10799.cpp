#include<iostream>
#include<string>

int main() {
    std::string str;
    std::cin >> str;
    int count = 0;
    int laser = 0;
    char before = ' ';
    int stack[100000] = {0,};
    int top = -1;
    for(int i = 0; i < str.size(); i++) {
        if(str[i] == '(') {
            top++;
            stack[top] = 0;
        } else {
            if(before == '(') {
                stack[top] = 1;
            } else {
                while(true) {
                    if(stack[top] == 0) {
                        stack[top] = laser;
                        count += laser+1;
                        laser = 0;
                        break;
                    } else {
                        laser += stack[top];
                        top--;
                    }
                }
            }
        }
        before = str[i];
    }
    std::cout << count<< std::endl;
    return 0;
}