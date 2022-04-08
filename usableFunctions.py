import random.randint from random

def asA():
    print("AAA")

def randomNumber(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound) * random.randint(lower_bound, upper_bound) - (0.5 * upper_bound - lower_bound)
