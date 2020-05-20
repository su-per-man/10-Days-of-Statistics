LH_UH = lambda n,mid : [n[0:mid],n[mid:]] if(len(n)%2==0) else [n[0:mid],n[mid+1:]]
median = lambda t,mid : sum(t[mid-1:mid+1])/2 if(len(t)%2==0) else t[mid]

n=int(input())
numbers=[int(x) for x in input().split(" ")]
freq=[int(x) for x in input().split(" ")]
del numbers[n:]
del freq[n:]
series=[]
for i in range(n):
    for _ in range(freq[i]):series.append(numbers[i])

series.sort()
l,h=LH_UH(series,int(len(series)/2))
print("%.1f"%(median(h,int(len(h)/2)) - median(l,int(len(l)/2))))
