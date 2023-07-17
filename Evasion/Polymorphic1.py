import random
import string

def generate_junk_function_cpp():
    num_iterations = random.randint(1000, 5000)

    code = f'''#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

class ComplexNumber {{
private:
    double real;
    double imaginary;

public:
    ComplexNumber(double real = 0.0, double imaginary = 0.0) : real(real), imaginary(imaginary) {{}}

    ComplexNumber operator+(const ComplexNumber& other) const {{
        return ComplexNumber(real + other.real, imaginary + other.imaginary);
    }}

    ComplexNumber operator-(const ComplexNumber& other) const {{
        return ComplexNumber(real - other.real, imaginary - other.imaginary);
    }}

    ComplexNumber operator*(const ComplexNumber& other) const {{
        return ComplexNumber(real * other.real - imaginary * other.imaginary, real * other.imaginary + imaginary * other.real);
    }}

    ComplexNumber operator/(const ComplexNumber& other) const {{
        double denominator = other.real * other.real + other.imaginary * other.imaginary;
        return ComplexNumber((real * other.real + imaginary * other.imaginary) / denominator, (imaginary * other.real - real * other.imaginary) / denominator);
    }}

    double getMagnitude() const {{
        return std::sqrt(real * real + imaginary * imaginary);
    }}

    ComplexNumber power(int exponent) const {{
        ComplexNumber result = *this;

        for (int i = 1; i < exponent; ++i) {{
            result = result * (*this);
        }}

        return result;
    }}

    void print() const {{
        if (real != 0.0 && imaginary != 0.0) {{
            std::cout << real << " + " << imaginary << "i";
        }}
        else if (real != 0.0) {{
            std::cout << real;
        }}
        else if (imaginary != 0.0) {{
            std::cout << imaginary << "i";
        }}
        else {{
            std::cout << "0";
        }}
    }}
}};

void junkFunction() {{
    std::srand(std::time(0));

    int numIterations = {num_iterations};

    char* junkMemory = new char[numIterations];
    for (int i = 0; i < numIterations; ++i) {{
        junkMemory[i] = std::rand() % 256;
    }}

    ComplexNumber* complexNumbers = new ComplexNumber[numIterations];
    for (int i = 0; i < numIterations; ++i) {{
        double real = std::rand() % 101 - 50;
        double imaginary = std::rand() % 101 - 50;
        complexNumbers[i] = ComplexNumber(real, imaginary);
    }}

    ComplexNumber sum;
    ComplexNumber product;
    double maxMagnitude = 0.0;
    int maxMagnitudeIndex = 0;

    for (int i = 0; i < numIterations; ++i) {{
        sum = sum + complexNumbers[i];
        product = product * complexNumbers[i];

        double magnitude = complexNumbers[i].getMagnitude();
        if (magnitude > maxMagnitude) {{
            maxMagnitude = magnitude;
            maxMagnitudeIndex = i;
        }}
    }}

    ComplexNumber powerResult = complexNumbers[maxMagnitudeIndex].power(std::rand() % 6 + 2);

    std::cout << "Sum of complex numbers: ";
    sum.print();
    std::cout << std::endl;

    std::cout << "Product of complex numbers: ";
    product.print();
    std::cout << std::endl;

    std::cout << "Complex number with the maximum magnitude: ";
    complexNumbers[maxMagnitudeIndex].print();
    std::cout << std::endl;

    std::cout << "Result of powering the complex number: ";
    powerResult.print();
    std::cout << std::endl;

    delete[] junkMemory;
    delete[] complexNumbers;
}}

int main() {{
    junkFunction();

    return 0;
}}
'''

    return code


def generate_cpp_script():
    cpp_code = generate_junk_function_cpp()
    return f'''{cpp_code}'''

