from datetime import datetime

S1 = list(input())
S2 = list(input())
#print(S1,S2)
if S1==S2:
    print("00:00:00")
else:
    
    s1=""
    s2=""
    for i in range(0,len(S1)):
        if S1[i]!='\r':
        
            s1=s1+S1[i]
        if S2[i]!='\r':
            s2=s2+S2[i]
    try:
    
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        tdelta=str(tdelta)

    except:
        pass
    ans=tdelta.split(" ")
    ans=ans[-1]    
    ans=ans.split(":")

    for i in range(0,len(ans)):
        if int(ans[i])<10:
            ans[i]="0"+str(int(ans[i]))
    print(":".join(ans))
