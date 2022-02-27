N = int(input())

limit = int(N**0.5)
for i in range(2,limit+1):
    if N%i==0:
        print("No")
        break
    elif i==limit:
        print("Yes")

