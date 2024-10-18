def algo(n):
    if n==1 or n==0:
        return
    elif n%2==0:
        print(int(n/2), end=" ")
        algo(int(n/2))
    elif n%2!=0:
        print(int(n*3+1),end=" ")
        algo(int(n*3+1))
n=int(input())
print(n, end=" ")
algo(n)