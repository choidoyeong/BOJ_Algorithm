#include<iostream>
#include <string>

int main() {
    int line = 0;
    std::cin >> line;
    for(int i = 0; i < line; i++) {
        int count = 0;
        std::string str;
        std::cin >> str;
        for(int j = 0; j < str.size(); j++) {
            if(str[j] == '(') {
                count++;
            } else {
                count--;
                if(count < 0) {
                    break;   
                }
            }
        }
        if(count == 0) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }
    return 0;
}