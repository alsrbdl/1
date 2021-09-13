#3,6,9
n=int(input())
i=1
s=0
while i <= n :
	if i%10==3 :
		print("X", end=' ')
	elif i%10==6 :
		print("X", end=' ')
	elif i%10==9 :
		print("X", end=' ')
	else : print(i, end=' ')
	i += 1
