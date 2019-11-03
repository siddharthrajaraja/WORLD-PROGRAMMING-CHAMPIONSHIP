t=int(input())
while t!=0:
    A=list(input())
    B=list(input())
    i=0
    cb=B[::]
    ans=[]
    while len(B)!=0:
        if len(A)==0:
            break
        
        if B[i].lower()==A[0].lower():
            ans.append(B[i])
            B.pop(i)
            
            A.pop(0)
        else:
            A.pop(0)    
    #print(ans,A)
    if ans==cb:
        flag=0
        
        if len(A)!=0:
            for i in range(0,len(A)):
                if ord(A[i]) in range(ord('A'),ord('Z')+1):
                    flag=1
                    break
        if flag==0:            
            print(1)
        else:
            print(0)
    else:
        print(0)
    t=t-1
