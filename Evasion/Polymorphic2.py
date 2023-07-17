import random
import string
import base64

# Generate a random variable name
def generate_variable_name():
    return ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))

# Generate a random C++ expression using specific variables
def generate_expression(variables):
    variable_name = random.choice(variables)
    expression = f"{variable_name} = {random.randint(1, 100)};\n"
    expression += f"cout << \"{variable_name}: \" << {variable_name} << endl;\n"
    return expression

# Generate a random complex C++ expression
def generate_complex_expression(variables):
    variable_name = random.choice(variables)
    expression = f"{variable_name} = (2 * ({variable_name} + {random.randint(1, 10)})) / {random.randint(1, 5)};\n"
    expression += f"cout << \"{variable_name}: \" << {variable_name} << endl;\n"
    return expression

# Generate random C++ junk code
def generate_cpp_junk_code(variables, additional_variables):
    code = "#include <iostream>\n"
    code += "#include <cstdlib>\n\n"
    code += "using namespace std;\n\n"
    code += "void* customMalloc(size_t size) {\n"
    code += "\tvoid* ptr = malloc(size);\n"
    code += "\tcout << \"Custom malloc called. Size: \" << size << \", Address: \" << ptr << endl;\n"
    code += "\treturn ptr;\n"
    code += "}\n\n"
    code += "void* customCalloc(size_t num, size_t size) {\n"
    code += "\tvoid* ptr = calloc(num, size);\n"
    code += "\tcout << \"Custom calloc called. Elements: \" << num << \", Size: \" << size << \", Address: \" << ptr << endl;\n"
    code += "\treturn ptr;\n"
    code += "}\n\n"
    code += "void customFree(void* ptr) {\n"
    code += "\tfree(ptr);\n"
    code += "\tcout << \"Custom free called. Address: \" << ptr << endl;\n"
    code += "}\n\n"
    code += "int main() {\n\n"
    code += "\t" + "// Variable pool\n"
    for variable in variables:
        code += f"\tint {variable} = 0;\n"
    code += "\n"
    code += "\t" + "// Additional variable pool\n"
    for var_type, variable in additional_variables:
        code += f"\t{var_type} {variable};\n"
    code += "\n"
    code += "\t" + "// Random expressions\n"
    for _ in range(random.randint(20, 30)):
        code += "\t" + generate_expression(variables)
    code += "\n"
    code += "\t" + "// Complex expressions\n"
    for _ in range(random.randint(10, 15)):
        code += "\t" + generate_complex_expression(variables)
    code += "\n"
    code += "\t" + "// Print variable values\n"
    for _ in range(random.randint(5, 10)):
        variable_name = random.choice(variables)
        code += f"\tcout << \"{variable_name}: \" << {variable_name} << endl;\n"
    code += "\n"
    code += "\t" + "// Loops and memory allocation\n"
    code += "\tint* ptr;\n"
    code += "\tfor (int i = 0; i < 10; i++) {\n"
    code += "\t\tint size = rand() % 100 + 1;\n"
    code += "\t\tptr = (int*)customMalloc(size * sizeof(int));\n"
    code += "\t\tfor (int j = 0; j < size; j++) {\n"
    code += "\t\t\t*(ptr + j) = rand() % 100;\n"
    code += "\t\t}\n"
    code += "\t\tcustomFree(ptr);\n"
    code += "\t}\n"
    code += "\n"
    code += "\t" + "// Obfuscated code\n"
    code += "\n"
    code += "\t" + "return 0;\n"
    code += "}"

    return code

def generate_code(): 
    # Generate variable pools
    variable_pool = [generate_variable_name() for _ in range(random.randint(5, 10))]
    additional_variable_pool = []
    for _ in range(random.randint(3, 5)):
        var_type = random.choice(["double", "float", "string"])
        variable = generate_variable_name()
        additional_variable_pool.append((var_type, variable))

    # Generate random C++ junk code
    cpp_junk_code = generate_cpp_junk_code(variable_pool, additional_variable_pool)
    return f'''{cpp_junk_code}'''
