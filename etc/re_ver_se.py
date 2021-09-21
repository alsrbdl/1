a=list(map(str, input().split('_')))
l=len(a)

for i in range(l) :
	b=a[i]
	print(''.join(reversed(b)), end='')
	if i<l-1 :
		print('_', end='')