#include "library.h"

#include <iostream>

class Hello {

public:
    void say() const {
        std::cout << "Hello, World!" << std::endl;
    }
};

void hello() {
    const auto h = Hello();
    h.say();
}


