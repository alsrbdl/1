#1부터 계속 더해 나갈 때, 입력값을 넘어서려면 어디까지 더해야 하나 계산
n=int(input())
c = 0
s = 0
while s < n :
	c = c+1
	s += c
print(c)