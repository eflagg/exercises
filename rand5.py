from random import randint

def rand5():

    random_num = 6

    while random_num > 5:
        random_num = randint(1,7)

    return random_num