arr=[1,0,0]
s=list(input())

    
for i in range(0,len(s)):
    if  s[i]=='A':
        t=arr[0]
        arr[0]=arr[1]
        arr[1]=t
        
    elif s[i]=='B':
        t=arr[1]
        arr[1]=arr[2]
        arr[2]=t
        
    elif  s[i]=='C':
        t=arr[2]
        arr[2]=arr[0]
        arr[0]=t
        
    #print(s[i],ind)
print(arr.index(1)+1)
