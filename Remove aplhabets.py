import numpy as np
s=list(input())
stri=list("CAMBRIDGE")
ans=""
for i in range(0,len(s)):
    ans=ans+s[i]
    ans=ans+" "
#print(ans)

for i in range(0,len(stri)):
    #print(ans)
    ans=ans.replace(stri[i]," ")
ans=list(ans)
ANS=[]
for i in range(0,len(ans)):
    if ans[i]!=" ":
        ANS.append(ans[i])
print("".join(ANS))
    

