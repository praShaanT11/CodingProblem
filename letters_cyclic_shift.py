# -*- coding: utf-8 -*-
"""Letters Cyclic Shift.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KzcQbQ2c5BXRjzW0v10QFDf6kYMB6-SD
"""

s=input()
si=list(s)
cnt=0
sl=len(s)
for i in range(len(s)):
  if si[i]=='a':
    cnt+=1
    continue
  elif(i+1<len(si) and si[i]!='a' and si[i+1]=='a' ):
    si[i]=chr(ord(si[i]) - 1)
    break
  else:
    si[i]=chr(ord(si[i]) - 1)
if(cnt==sl):
  si[sl-1]='z'

print(''.join(si))

