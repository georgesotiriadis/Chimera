import random
import os
import string

def junk(size):
    remaining_size = size
    random_data = ""

    # Generate and write random data until reaching the desired file size
    while remaining_size > 0:
        # Determine the size of the chunk to generate (maximum 10 MB)
        chunk_size = min(remaining_size, 10 * 1024 * 1024)
            
        # Generate random data of chunk_size
        hexed = os.urandom(chunk_size)
        
        #Convert them to hex and add them into the previously generated data
        random_data = random_data + hexed.hex()
            
        # Update the remaining size
        remaining_size = remaining_size - chunk_size
    
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits

    # Generate a random string of specified length
    length = random.choice(range(6,30))
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    #Create a variable to include in the template
    variable = f"""
        {random_string}="{random_data}"
    """
    
    return variable
