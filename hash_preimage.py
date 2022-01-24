import hashlib
import os
import string
import random

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    
    k = len(target_string)
    characters = string.ascii_lowercase
    characters = characters + string.ascii_uppercase
    characters = characters + string.digits
    characters = characters + string.punctuation

    x = get_string(20,characters)
    x_bits = get_bits(x,k)
    while (x_bits != target_string):
        x = get_string(20,characters)
        x_bits = get_bits(x,k)

    x = x.encode('utf-8')
    return( x )


def get_bits(string, k):
    hex_str = hashlib.sha256(string.encode('utf-8')).hexdigest()
    bit_str = bin(int(hex_str, 16)).zfill(8)
    return(bit_str[-k:])

def get_string(length, characters):
    
    string = ''.join(random.choice(characters) for i in range(length))
    return string

#hash_preimage("010")