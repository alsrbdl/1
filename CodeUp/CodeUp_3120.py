a, b = map(int, input().split())
c = abs(a-b)
d = 0
e = 0

if (c>10):
  d = c // 10
  e += d
  c -= d*10
  c = abs(c)
if (c>7):
  c = abs(c-10)
  e += 1
if (c>5):
  c = abs(c-5)
  e += 1
if (c>3):
  c = abs(c-5)
  e += 1

print(c+e)