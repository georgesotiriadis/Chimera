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
    obfuscated_code = generate_expression(variables)
    obfuscated_code = base64.b64encode(obfuscated_code.encode()).decode()
    code += f"\tcout << \"Obfuscated code: \" << {obfuscated_code} << endl;\n"
    code += "\n"
    code += "\t" + "return 0;\n"
    code += "}"

    return code

# Generate polymorphic Python code
def generate_polymorphic_python_code(variables, additional_variables):
    code = "import random\n"
    code += "import string\n"
    code += "import base64\n\n"
    code += "def generate_variable_name():\n"
    code += "    return ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))\n\n"
    code += "def generate_expression(variables):\n"
    code += "    variable_name = random.choice(variables)\n"
    code += "    expression = f\"{variable_name} = {random.randint(1, 100)};\\n\"\n"
    code += "    expression += f\"print('{variable_name}:', {variable_name})\\n\"\n"
    code += "    return expression\n\n"
    code += "def generate_complex_expression(variables):\n"
    code += "    variable_name = random.choice(variables)\n"
    code += "    expression = f\"{variable_name} = (2 * ({variable_name} + {random.randint(1, 10)})) / {random.randint(1, 5)};\\n\"\n"
    code += "    expression += f\"print('{variable_name}:', {variable_name})\\n\"\n"
    code += "    return expression\n\n"
    code += "def generate_cpp_junk_code(variables, additional_variables):\n"
    code += "    code = \"#include <iostream>\\n\"\n"
    code += "    code += \"#include <cstdlib>\\n\\n\"\n"
    code += "    code += \"using namespace std;\\n\\n\"\n"
    code += "    code += \"void* customMalloc(size_t size) {\\n\"\n"
    code += "    code += \"    void* ptr = malloc(size);\\n\"\n"
    code += "    code += \"    cout << 'Custom malloc called. Size: ' << size << ', Address: ' << ptr << endl;\\n\"\n"
    code += "    code += \"    return ptr;\\n\"\n"
    code += "    code += \"}\\n\\n\"\n"
    code += "    code += \"void* customCalloc(size_t num, size_t size) {\\n\"\n"
    code += "    code += \"    void* ptr = calloc(num, size);\\n\"\n"
    code += "    code += \"    cout << 'Custom calloc called. Elements: ' << num << ', Size: ' << size << ', Address: ' << ptr << endl;\\n\"\n"
    code += "    code += \"    return ptr;\\n\"\n"
    code += "    code += \"}\\n\\n\"\n"
    code += "    code += \"void customFree(void* ptr) {\\n\"\n"
    code += "    code += \"    free(ptr);\\n\"\n"
    code += "    code += \"    cout << 'Custom free called. Address: ' << ptr << endl;\\n\"\n"
    code += "    code += \"}\\n\\n\"\n"
    code += "    code += \"int main() {\\n\\n\"\n"
    code += "    code += \"\\t\" + \"// Variable pool\\n\"\n"
    for variable in variables:
        code += f"    code += \"\\tint {variable} = 0;\\n\"\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"// Additional variable pool\\n\"\n"
    for var_type, variable in additional_variables:
        code += f"    code += \"{var_type} {variable};\\n\"\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"// Random expressions\\n\"\n"
    for _ in range(random.randint(20, 30)):
        code += "    code += \"\\t\" + generate_expression(variables)\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"// Complex expressions\\n\"\n"
    for _ in range(random.randint(10, 15)):
        code += "    code += \"\\t\" + generate_complex_expression(variables)\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"// Print variable values\\n\"\n"
    for _ in range(random.randint(5, 10)):
        variable_name = random.choice(variables)
        code += f"    code += \"\\tcout << '{variable_name}: ' << {variable_name} << endl;\\n\"\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"// Loops and memory allocation\\n\"\n"
    code += "    code += \"\\tint* ptr;\\n\"\n"
    code += "    code += \"\\tfor (int i = 0; i < 10; i++) {\\n\"\n"
    code += "    code += \"\\t\\tint size = rand() % 100 + 1;\\n\"\n"
    code += "    code += \"\\t\\tptr = (int*)customMalloc(size * sizeof(int));\\n\"\n"
    code += "    code += \"\\t\\tfor (int j = 0; j < size; j++) {\\n\"\n"
    code += "    code += \"\\t\\t\\t*(ptr + j) = rand() % 100;\\n\"\n"
    code += "    code += \"\\t\\t}\\n\"\n"
    code += "    code += \"\\t\\tcustomFree(ptr);\\n\"\n"
    code += "    code += \"\\t}\\n\"\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"// Obfuscated code\\n\"\n"
    obfuscated_code = generate_expression(variables)
    obfuscated_code = base64.b64encode(obfuscated_code.encode()).decode()
    code += f"    code += \"\\tcout << 'Obfuscated code: ' << {obfuscated_code} << endl;\\n\"\n"
    code += "    code += \"\\n\"\n"
    code += "    code += \"\\t\" + \"return 0;\\n\"\n"
    code += "    code += \"}\""
    code += "    return code\n\n"
    code += f"print(generate_cpp_junk_code([" + ', '.join([f"'{variable}'" for variable in variables]) + "], ["
    code += ', '.join([f"('{var_type}', '{variable}')" for var_type, variable in additional_variables]) + "]))\n"

    return code

# Generate variable pools
variable_pool = [generate_variable_name() for _ in range(random.randint(5, 10))]
additional_variable_pool = []
for _ in range(random.randint(3, 5)):
    var_type = random.choice(["double", "float", "string"])
    variable = generate_variable_name()
    additional_variable_pool.append((var_type, variable))

# Generate polymorphic Python code with random C++ junk code
polymorphic_python_code = generate_polymorphic_python_code(variable_pool, additional_variable_pool)
cpp_junk_code = generate_cpp_junk_code(variable_pool, additional_variable_pool)

print(polymorphic_python_code)
print("------")
print(cpp_junk_code)
