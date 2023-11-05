import random
import string

def generate_junk_function_cpp():
    num_iterations = random.randint(1000, 5000)
    
    value1 = random.choice(range(1,100000))

    value2 = random.choice(range(1,100000))
    
    
    code = f'''

class ComplexNumber{str(value1)} {{
private:
    double real;
    double imaginary;

public:
    ComplexNumber{str(value1)}(double real = 0.0, double imaginary = 0.0) : real(real), imaginary(imaginary) {{}}

    ComplexNumber{str(value1)} operator+(const ComplexNumber{str(value1)}& other) const {{
        return ComplexNumber{str(value1)}(real + other.real, imaginary + other.imaginary);
    }}

    ComplexNumber{str(value1)} operator-(const ComplexNumber{str(value1)}& other) const {{
        return ComplexNumber{str(value1)}(real - other.real, imaginary - other.imaginary);
    }}

    ComplexNumber{str(value1)} operator*(const ComplexNumber{str(value1)}& other) const {{
        return ComplexNumber{str(value1)}(real * other.real - imaginary * other.imaginary, real * other.imaginary + imaginary * other.real);
    }}

    ComplexNumber{str(value1)} operator/(const ComplexNumber{str(value1)}& other) const {{
        double denominator = other.real * other.real + other.imaginary * other.imaginary;
        return ComplexNumber{str(value1)}((real * other.real + imaginary * other.imaginary) / denominator, (imaginary * other.real - real * other.imaginary) / denominator);
    }}

    double getMagnitude() const {{
        return sqrt(real * real + imaginary * imaginary);
    }}

    ComplexNumber{str(value1)} power(int exponent) const {{
        ComplexNumber{str(value1)} result = *this;

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

void junkFunction{str(value2)}() {{
    srand(time(0));

    int numIterations = 10;

    char* junkMemory = new char[numIterations];
    for (int i = 0; i < numIterations; ++i) {{
        junkMemory[i] = rand() % 256;
    }}

    ComplexNumber{str(value1)}* complexNumbers = new ComplexNumber{str(value1)}[numIterations];
    for (int i = 0; i < numIterations; ++i) {{
        double real = rand() % 101 - 50;
        double imaginary = rand() % 101 - 50;
        complexNumbers[i] = ComplexNumber{str(value1)}(real, imaginary);
    }}

    ComplexNumber{str(value1)} sum;
    ComplexNumber{str(value1)} product;
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

    ComplexNumber{str(value1)} powerResult = complexNumbers[maxMagnitudeIndex].power(rand() % 6 + 2);

    // Do whatever you want with the results here

}}


void junkFunction{str(value2)}();

'''

    return code


def generate_cpp_script():
    cpp_code = generate_junk_function_cpp()
    return cpp_code
