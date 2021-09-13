#그림 파일 용량 계산
h,b,c=map(int, input().split())
n=(h*b*c)/1024/1024/8
print(format(n, ".2f"),'MB')