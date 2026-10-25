N = int(input())
P = int(input())

if N <= 0 or P <= 0:
    print("Invalid input")
else:
    result = 1
    i = 1
    while i <= P:
        result = result*N
        i += 1
    print(result)