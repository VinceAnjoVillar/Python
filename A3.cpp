#include <iostream>
#include <cmath>

using namespace std;

struct Circle {
    float radius;
};

float computeCircumference(const Circle& circle) {
    return 2 * M_PI * circle.radius;
}

float computeArea(const Circle& circle) {
    return M_PI * pow(circle.radius, 2);
}

int main() {
    Circle circle1;
    
    cout << "Enter the radius of the circle: ";
    cin >> circle1.radius;

    float circumference = computeCircumference(circle1);
    float area = computeArea(circle1);

    cout << "Circumference: " << circumference << endl;
    cout << "Area: " << area << endl;
    
    return 0;
}
