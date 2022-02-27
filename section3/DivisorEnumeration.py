N = int(input())

limit = int(N**0.5)

devisors = []
for i in range(1,limit+1):
    if N%i==0:
        devisors.append(i)
        if i!=N//i: 
            devisors.append(N//i)

devisors.sort()
for i in devisors:
    print(i)
