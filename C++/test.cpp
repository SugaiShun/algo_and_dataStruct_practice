#include <iostream>
#include <string>

int main(void)
{
    std::string name;
    std::cout << "what is your name ?";
    getline(std::cin,name);
    std::cout << "Hello," << name << "!" << std::endl;
}
