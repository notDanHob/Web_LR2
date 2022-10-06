def pow(n): 
    return n**2

def cache(func):
    cache = {}
    def inner(n):
        nonlocal cache
        if n not in cache:
            print('not cached')
            cache[n] = func(n)
            return cache[n]
        print('cached')
        return cache[n]
    return inner
dec = cache(pow)
while True:
    print(dec(int(input('Enter int n:'))))
