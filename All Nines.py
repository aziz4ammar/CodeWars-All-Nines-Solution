def all_nines(x):
    if x % 2 == 0 or x % 5 == 0:
        return -1
    
    n = 1
    num = 9
    
    while True:
        if num % x == 0:
            return num // x
        n += 1
        num = num * 10 + 9