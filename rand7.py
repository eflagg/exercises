from random import randint

def rand7():

    results = [ [1,2,3,4,5],
                [6,7,1,2,3],
                [4,5,6,7,1],
                [2,3,4,5,6],
                [7,1,2,3,4] ]
    
    x = randint(1,5) - 1
    y = randint(1,5) - 1
    
    while x == 4 and y > 0:
        x = randint(1,5) - 1
        y = randint(1,5) - 1
    
    return results[x][y]

def rand7_no_list():
    
    while True:
        x = randint(1,5) - 1
        y = randint(1,5) - 1
        
        outcome_num = ((x * 5) + y) + 1
        
        if outcome_num > 21:
            continue

        return (outcome_num % 7) + 1