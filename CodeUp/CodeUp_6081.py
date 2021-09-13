#1~n까지 숫자에 n을 곱하면 나오는 수 출력
m=input()
n=int(m, 16)
i=1
while i < 16 :
	print('%X'%n,'*%X'%i,'=%X'%(n*i),sep='')
	i += 1 