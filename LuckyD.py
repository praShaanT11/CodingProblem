lucky_number=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]

n=int(input())
count=0
for i in lucky_number:
    if n%i==0:
        count+=count
if count>0:
    print('YES')
else:
    print('NO')