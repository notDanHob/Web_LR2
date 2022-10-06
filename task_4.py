from time import sleep

def Newton(n=int(input('Enter n: ')),A=int(input('Enter A: '))):
    x0 = 2
    x = 1
    while x0!=x:
        x0=x
        x = 1/n*((n-1)*x0+A/x0**(n-1))
    return x

print(Newton())