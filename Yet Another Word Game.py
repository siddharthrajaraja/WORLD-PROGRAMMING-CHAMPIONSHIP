## Read input as specified in the question.
## Print output as specified in the question.
#Write your code here
t=int(input())
arr=[]
pointer=[]
for i in range(0,26):
    arr.append([])
    pointer.append(0)
    
while t!=0:
    s=input()
    ind=abs(ord('a')-ord(s[0]))
    arr[ind].append(s)
    arr[ind].sort()
    
    t=t-1
choices=list(map(str,input().split()))

for i in range(0,len(choices)):
    ind=abs(ord('a')-ord(choices[i]))
    print(arr[ind][pointer[ind]])
    
    pointer[ind]=(pointer[ind]+1)%len(arr[ind])
    
