N = int(input())
D = int(input())
count = 0

while N > 0:
    digit = N%10
    if digit == D:
        count += 1
    N = N//10
print(count)