import math
a,b,v = map(int, input().split())

d = math.ceil(v-b)/(a-b)
if (d*(a-b)-b)>=v:
  print(d-1)
else:
  print(math.ceil(d))
