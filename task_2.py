def spread(a = [int(x) for x in input().split()]):
    d2,d3,d5 = [],[],[]
    for x in a:
        if x%2==0:d2.append(x)
        if x%3==0:d3.append(x)
        if x%5==0:d5.append(x)
    print(
        '\nDivisible by 2:',*d2,
        '\nDivisible by 3:',*d3,
        '\nDivisible by 5:',*d5
        )
spread()