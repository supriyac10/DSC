n=int(input())
ar=[int(input()) for a in range(0,n)]
ar.sort()
a=0
pair=0
for b in range(0,n):
    if len(ar)==0:
        break
    else:
        b=ar.pop(0)
        if a==b:
            pair=pair+1
            a="sit"
        else:
            a=b
print(pair)
