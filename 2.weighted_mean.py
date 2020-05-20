def mean(n,c):
    return round(sum(n[i]*c[i] for i in range(len(n)))/sum(c),1)

n=int(input())
numbers=[int(x) for x in input().split(" ")]
counts=[int(x) for x in input().split(" ")]
del numbers[n:]
del counts[n:]
print(mean(numbers,counts))
