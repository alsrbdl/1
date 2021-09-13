#n까지 적힌 주사위, m까지 적힌 주사위 던질 때 나오는 경우의 수 모두 출력
n,m=map(int, input().split())
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)