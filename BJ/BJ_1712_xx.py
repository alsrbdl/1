a,b,c=map(int, input().split())
n=int()
if b>c : 
	print('-1')
elif b=c:
	print('0')
else:
	print(a//(c-b)+1)
