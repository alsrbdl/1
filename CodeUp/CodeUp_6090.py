#?
a,m,d,n=map(int, input().split())
while n>1 :
	a=a*m+d
	n=n-1
print(a)