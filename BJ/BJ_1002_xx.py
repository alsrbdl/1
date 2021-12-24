import math
t=int(input())
s=[[0]* 6 for _ in range(t)]
s=[list(map(int, input().split())) for _ in range(t)]
for i in range (t) :
	if s[i][0]==s[i][3] and s[i][1]==s[i][4] and s[i][2]==s[i][5] :
		print('-1')	
		break
	if s[i][0]==s[i][3] and s[i][1]==s[i][4] and s[i][2]!=s[i][5] :
		print('0')	
		break
	d=math.sqrt((s[i][0]-s[i][3])**2 + (s[i][1] - s[i][4])**2)
	v=s[i][2] + s[i][5]
	if d > v :
		print('0')
		break
	if (d+s[i][2]) < s[i][5] or (d+s[i][5]) < s[i][2] or (s[i][2]+s[i][5]) < d :
		print('0')
		break
	if d == v or d == (s[i][2]-s[i][5]) or d == (s[i][5] - s[i][2]):
		print('1')
	else : print('2')	