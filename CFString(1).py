n = int(input())  
s = list(input().strip())
valid=int(n/4)
countA=0
countC=0

countG=0
countT=0

if (len(s)%4!=0):
    print('===')
elif (len(s)%4==0):
    for i in range(len(s)):
        if s[i]=='A':
            countA+=1
        elif s[i]=='C':
            countC+=1
        elif s[i]=='G':
            countG+=1
        elif s[i]=='T':
            countT+=1
    if (countA>valid or countC>valid or countG>valid or countT>valid):
        print('===')
    else:
        for j in range(len(s)):
            if (s[j]=='?' and countA<valid):
                s[j]='A'
                countA+=1
            elif (s[j]=='?' and countC<valid):
                s[j]='C'
                countC+=1
            elif (s[j]=='?' and countG<valid):
                s[j]='G'
                countG+=1
            elif (s[j]=='?' and countT<valid):
                s[j]='T'
                countT+=1
        print("".join(s))
                