#입력한 수 까지 짝수 합 계산
n=int(input())
s = 0
for i in range(1, n+1) :
	if i%2==0 :
		s += i
print(s)