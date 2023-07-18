import random
import string

def generate_junk_function_cpp():
    num_iterations = random.randint(1000, 5000)

    value = random.choice(range(1,100))
    
    code = f'''

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
        return sqrt(real * real + imaginary * imaginary);
    }}

    ComplexNumber power(int exponent) const {{
        ComplexNumber result = *this;

        for (int i = 1; i < exponent; ++i) {{
            result = result * (*this);
        }}

        return result;
    }}

    char* toString() {{
    const int bufferSize = 256;
    char* output = new char[bufferSize];
    output[0] = '\0';

    if (real != 0.0 && imaginary != 0.0) {{
        snprintf(output, bufferSize, "%.2f + %.2fi", real, imaginary);
    }}
    else if (real != 0.0) {{
        snprintf(output, bufferSize, "%.2f", real);
    }}
    else if (imaginary != 0.0) {{
        snprintf(output, bufferSize, "%.2fi", imaginary);
    }}
    else {{
        snprintf(output, bufferSize, "0");
    }}

    return output;
    }};
}};

void junkFunction{str(value)}() {{
    srand(time(0));

    int numIterations = 10;

    char* junkMemory = new char[numIterations];
    for (int i = 0; i < numIterations; ++i) {{
        junkMemory[i] = rand() % 256;
    }}

    ComplexNumber* complexNumbers = new ComplexNumber[numIterations];
    for (int i = 0; i < numIterations; ++i) {{
        double real = rand() % 101 - 50;
        double imaginary = rand() % 101 - 50;
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

    ComplexNumber powerResult = complexNumbers[maxMagnitudeIndex].power(rand() % 6 + 2);

    // Do whatever you want with the results here

}}


void junkFunction{str(value)}();

'''

    return code


def generate_cpp_script():
    cpp_code = generate_junk_function_cpp()
    return cpp_code
