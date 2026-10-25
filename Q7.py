N = int(input())
if N <= 0:
    print("Invalid input")
else:
    sum = 0
    i = 1
    while i < N:
        if N%i == 0:
            sum = sum +i
        i += 1
        
    if sum == N:
        print("Perfect number")
    else:
        print("Not a Perfect number")