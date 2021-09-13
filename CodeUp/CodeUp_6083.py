#rgb 경우의 수
r,g,b=map(int, input().split())
for i in range(r):
	for j in range(g):
		for k in range(b):
			print(i, j, k)
print(r*g*b)