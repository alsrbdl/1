#행의 갯수가 t, 열의 갯수가 q인 2차원 배열 입력 받고 출력하기
t,q=map(int, input().split())
s=[[0]* q for _ in range(t)]
s=[list(map(int, input().split())) for _ in range(t)]
print(s)