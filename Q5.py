N = int(input())
M = int(input())

original = N
reverse = 0

while N > 0:
    digit = N%10
    reverse = reverse*10+digit
    N = N//10

if reverse == M:
    print("Yes")
else:
    print("No")