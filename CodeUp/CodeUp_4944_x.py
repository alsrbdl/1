n,l,r=map(int, input().split())
a=list(map(int, input().split()))
s=int()

if (l>2*r*n) :
	print('-1이다')

else :			
	if (a[0] + r > l) :
		s=l - a[n-1] - r	
		print('경계실패')
	else :
		for i in range(1,n) :
			if (a[i] - a[i-1]>2*r) : 
				k=a[i+1] - a[i] - 2*r
				s=a[i]+k
	print(s)
	
# 0~L구간
# 구간 위 점에 N개의 센서
# 센서 식별 범위는 r
# 점p 위 센서는 p-r ~ p+r 식별구간
# a[i] - a[i-1]>2r, 
#  