def missing_number(n,num):
    num=set(num)
    for x in range(1,n+1):
        if x not in num:
            return x

n = int(input())
num = list(map(int, input().strip().split()))

missing = missing_number(n, num)
print(missing)
