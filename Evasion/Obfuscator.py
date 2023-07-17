import random
import secrets

from Evasion.Junk import junk
from Evasion.JitterSleeper import jitterSleeper
from Evasion.Polymorphic1 import generate_cpp_script
from Evasion.Polymorphic2 import generate_code

def obfuscatorArray(time):
    
    #Use random time if got the default value (4000)
    if time == 4000:
        # Create an instance
        rng = random.SystemRandom()
        # Generate an array with random numbers
        array_size = 30
        min_value = 1
        max_value = 5
        random_array = [rng.randint(min_value, max_value) for _ in range(array_size)]
        return random_array
    #Else use the given time into an array
    else:
        # Create an instance of random.SystemRandom()
        rng = random.SystemRandom()
        positions = 30
        # Calculate the initial value for each position
        initial_value = time // positions

        # Calculate the remaining value
        remaining_value = time % positions

        # Create an array to store the values
        array = []

        # Generate values for each position
        for _ in range(positions):
            # Add the initial value to the array
            array.append(initial_value)

        # Randomly distribute the remaining value across the positions
        for _ in range(remaining_value):
            # Generate a random index
            random_index = rng.randrange(positions)
            # Add 1 to the value at the random index
            array[random_index] += 1

        return array

def obfuscatorSize(size):
    
    #If got the default value (0)
    if size == 0:
        # Specify the number of positions and the desired value
        num_positions = 30
        value = size

        # Generate the array using list comprehension
        array = [value for _ in range(num_positions)]
        return array
    #Else generate random filesizes
    else:
        if size == 1:
            # Create an instance
            rng = random.SystemRandom()
            # Generate an array with random numbers
            #KB values
            array_size = 30
            min_value = 1000
            max_value = 10000
            random_array = [rng.randint(min_value, max_value) for _ in range(array_size)]
            return random_array
        #Separates in multiple values the give filesize
        else:
            # Create an instance of random.SystemRandom()
            rng = random.SystemRandom()
            positions = 30
            # Calculate the initial value for each position
            initial_value = size // positions

            # Calculate the remaining value
            remaining_value = size % positions

            # Create an array to store the values
            array = []

            # Generate values for each position
            for _ in range(positions):
                # Add the initial value to the array
                array.append(initial_value)

            # Randomly distribute the remaining value across the positions
            for _ in range(remaining_value):
                # Generate a random index
                random_index = rng.randrange(positions)
                # Add 1 to the value at the random index
                array[random_index] += 1

            return array

def obfuscator(value,size,disable):
    #Random polymorphic choice
    polymorphic = [generate_cpp_script(),generate_code()]
    #Disable filesize and junk data generation
    if size == 0 :
        random_obf = [jitterSleeper(value),secrets.choice(polymorphic)]
    #Disable sleep for domagic
    elif disable == 1 and size == 0 :
        random_obf = [secrets.choice(polymorphic)]
    elif disable == 1 and size != 0:
        random_obf = [junk(size),secrets.choice(polymorphic)]
    #Else we need junk data
    else:
        random_obf = [junk(size),jitterSleeper(value),secrets.choice(polymorphic)]
    
    #Randomly select obfuscation method
    selection = secrets.choice(random_obf)
    
    return selection
