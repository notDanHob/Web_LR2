from math import sqrt

def FindPrime(n=int(input('Enter n: '))):
    k = 2
    while k<sqrt(n):
        if n%k==0: return False
        k+=1
    return True

print(FindPrime())