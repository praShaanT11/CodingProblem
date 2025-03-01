n=int(input())
str=[]
for _ in range(n):
    s=input()
    str.append(s)
count=0
for i in str:
    if i=="Tetrahedron":
        count+=4
    elif i=="Cube":
        count+=6
    elif i=="Octahedron":
        count+=8
    elif i=="Dodecahedron":
        count+=12
    elif i=="Icosahedron":
        count+=20
    else:
        count+=0

print(count)