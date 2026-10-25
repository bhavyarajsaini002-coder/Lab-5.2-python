N = int(input())
count = 0

for i in range(1,N+1):
    if N%i == 0:
        print(i)
        count += 1
print("Total divisors:",count)


if count == 2:
    print("Prime number")
else:
    print("Not a Prime number")