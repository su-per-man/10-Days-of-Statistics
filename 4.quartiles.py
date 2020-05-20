LH_UH = lambda n,mid : [n[0:mid],n[mid:]] if(len(n)%2==0) else [n[0:mid],n[mid+1:]]
median = lambda t,mid : int(sum(t[mid-1:mid+1])/2) if(len(t)%2==0) else t[mid]

n=int(input())
numbers=[int(x) for x in input().split(" ")]
del numbers[n:]
numbers.sort()
l,h=LH_UH(numbers,int(n/2))
print(median(l,int(len(l)/2)))
print(median(numbers,int(len(numbers)/2)))
print(median(h,int(len(h)/2)))
