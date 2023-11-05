import random
import string
import re
from lorem.text import TextLorem

def junk(size):
    # separate words by ','
    # sentence length should be between 300 and 500
    size1 = 0
    
    if size == 1:
        lorem = TextLorem(wsep=',', srange=(0,1))
        s1 = lorem.sentence()
    
    if size > 1:
        left = random.randrange(random.randrange(1,5),random.randrange(5,10))
        right = random.randrange(random.randrange(50,100),random.randrange(100,200))
        size1 = random.randrange(int(size1)+left,int(size)+right)
        
        if size > size1:
            lorem = TextLorem(wsep=',', srange=(int(size1),int(size)))
            s1 = lorem.sentence()
        elif size1 > size:
            lorem = TextLorem(wsep=',', srange=(int(size),int(size1)))
            s1 = lorem.sentence()
        elif size1 == size:
            lorem = TextLorem(wsep=',', srange=(int(size),int(size1)+random.randrange(5,100)))
            s1 = lorem.sentence()
        
    # Define the characters to choose from
    characters = string.ascii_letters

    # Generate a random string of specified length
    length = random.choice(range(6,30))
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    #Fix issue c2026
    random_data = '"\n"'.join(re.findall(r'.{1,1024}', s1))
    
    #Create a variable to include in the template
    words = f""" {s1.split(",")} """
    words = words.replace("[","{")
    words = words.replace("]","}")
    words = words.replace("'","\"")
    variable = f"""
        string {random_string}[{s1.count(',')+1}] = {words};
    """
    
    return variable
