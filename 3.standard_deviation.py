import math

mean=lambda t : sum(t)/len(t)
std_dev = lambda mu,numbers : math.sqrt(sum((x-mu)**2 for x in numbers)/len(numbers))

n=int(input())
numbers=[int(i) for i in input().split(" ")]
print (round(std_dev(mean(numbers),numbers),1))
