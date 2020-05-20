def mean(t):
    return sum(t)/len(t)

def median(t):
    if(len(t)%2==0):
        l=int(len(t)/2)
        return(sum(t[l-1:l+1])/2)
    else:
        return(t[int(len(t)/2)])

def mode(t):
    maxFeq=0
    val=0
    for i in range(len(t)-1,-1,-1):
        if t.count(t[i]) >= maxFeq:
            maxFeq=t.count(t[i])
            val=t[i]
    return val

n=int(input())
temp=[int(x) for x in input().split(" ")]
del temp[n:]
temp.sort()
print(mean(temp))
print(median(temp))
print(mode(temp))
