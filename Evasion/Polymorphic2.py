import random
import string
import base64

# Generate a random variable name
def generate_variable_name():
    return ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10)))

# Generate a random C++ expression using specific variables
def generate_expression(variables):
    variable_name = random.choice(variables)
    expression = f"{variable_name} += {random.randint(1, 100)};\n"
    return expression

# Generate a random complex C++ expression
def generate_complex_expression(variables):
    variable_name = random.choice(variables)
    expression = f"{variable_name} = (2 * ({variable_name} + {random.randint(1, 10)})) / {random.randint(1, 5)};\n"
    return expression

# Generate random C++ junk code
def generate_cpp_junk_code(variables, additional_variables):
    value1 = random.choice(range(1,100))
    code = "\tint num"+str(value1)+" = "+str(value1)+";\n"
    code += "\tint size"+str(value1)+" = "+str(value1)+";\n"
    code += "\tunsigned long long* ptr"+str(value1)+";\n"
    code += "\nunsigned long long* ptr"+str(value1)+";\n"
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
        code += f"\t// {variable_name}: " + variable_name + "\n"
    code += "\n"
    code += "\t" + "// Loops and memory allocation\n"
    code += "\tint* ptr"+str(value1)+";\n"
    code += "\tfor (int i"+str(value1)+" = 0; i"+str(value1)+" < 10; i"+str(value1)+"++) {\n"
    code += "\t\tint size"+str(value1)+" = rand() % 100 + 1;\n"
    code += "\t\t*ptr"+str(value1)+" = (size"+str(value1)+" * sizeof(int));\n"
    code += "\t\tfor (int j"+str(value1)+" = 0; j"+str(value1)+" < size"+str(value1)+"; j"+str(value1)+"++) {\n"
    code += "\t\t\t(j"+str(value1)+") = rand() % 100;\n"
    code += "\t\t}\n"
    code += "\t}\n"
    code += "\n"
    code += "\t" + "// Obfuscated code\n"
    code += "\n"
    code += "\n"

    return code

def generate_code(): 
    # Generate variable pools
    variable_pool = [generate_variable_name() for _ in range(random.randint(5, 10))]
    additional_variable_pool = []
    for _ in range(random.randint(3, 5)):
        var_type = random.choice(["double", "float", "int"])
        variable = generate_variable_name()
        additional_variable_pool.append((var_type, variable))

    # Generate random C++ junk code
    cpp_junk_code = generate_cpp_junk_code(variable_pool, additional_variable_pool)
    return f'''{cpp_junk_code}'''
