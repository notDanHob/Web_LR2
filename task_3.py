def reversed_int(a=int(input('Enter int: '))):
    return int(''.join(reversed(str(abs(a)))))*int(a/abs(a))

print(reversed_int())