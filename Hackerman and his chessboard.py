r,c=map(int,input().split())
a,b=map(int,input().split())

firstrow=('X'*b+'.'*b)*b
FR=""

firstrow=firstrow*(c*b//2)

for i in range(0,c*b):
    try:
        
        FR=FR+firstrow[i]
    except:
        pass
firstrow=FR

    
invert=('.'*b+'X'*b)*b

IR=""

invert=invert*((c*b)//2)


for i in range(0,c*b):
    try:
        
        IR=IR+invert[i]
    except:
        pass
invert=IR

    

ans=[]

for i in range(0,r*a):
    ca=a
    while ca!=0 and i<r*a:
        #print(firstrow)
        ans.append(firstrow)
        ca=ca-1
        i=i+1
    ca=a
    while ca!=0 and i<r*a:
        #print(invert)
        ans.append(invert)
        ca=ca-1
        i=i+1
for i in range(0,r*a):
    print(ans[i])



