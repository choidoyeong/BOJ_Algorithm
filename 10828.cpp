#include<iostream>
#include<string>

int main() {
    int line = 0;
    std::cin >> line;
    int stack[line] = {0,};
    int top = -1;
    for(int i = 0; i < line; i++) {
        std::string command;
        std::cin >> command;
        if(command == "push") {
            int num;
            std::cin >> num;
            top++;
            stack[top] = num;
        } else if(command == "pop") {
            if(top ==  -1) {
                std::cout << -1 << std::endl;
            } else {
                std::cout << stack[top] << std::endl;
                top--; 
            }
        } else if(command == "size") {
            std::cout << top+1 << std::endl;
        } else if(command == "empty") {
            int boolean = top < 0 ? 1 : 0;
            std::cout << boolean << std::endl;
        } else if(command == "top") {
            if(top == -1) {
                std::cout << -1 << std::endl;
            } else {
                std::cout << stack[top] << std::endl;
            }
        }
    }
    return 0;
}