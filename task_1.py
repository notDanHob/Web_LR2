def check(a):return (a == a[::-1])

print(check(str(abs(int(input("Enter verification number:"))))))