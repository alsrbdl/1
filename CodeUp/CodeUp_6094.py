#입력된 수 중 가장 작은 수 찾기
s=int()
n=int(input())
a=list(map(int, input().split()))
s=a[0]
for i in range (n) :
	if a[i] < s :
		s=a[i]
		continue
print(s)