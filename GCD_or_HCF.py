def hcfnaive(a, b):
	if(b == 0):
		return abs(a)
	else:
		return hcfnaive(b, a % b)

a,b=map(int,input().split())
print(end="")
print(hcfnaive(a,b))
