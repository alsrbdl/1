c = int(input())
for i in range(c):
  count=0
  a=list(map(int, input().split()))
  avg=(sum(a[1:]))/(a[0])
  for j in a[1:]:
    if j>avg:
      count+=1
  p=count*100/a[0]
  print(f'{p:.3f}%')