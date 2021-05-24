import random
import math

def is_prime(num): 
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    a = random.randint(1, num-1)

    if pow(a, num-1) % num != 1:
        return False

    return True

def is_prime2(num):
    
    a = random.randint(1, num-1)

    return True if num == 2 else False
    
    return False if num % 2 == 0 or pow(a, num-1) % num != 1 else True




print(is_prime2(3))


