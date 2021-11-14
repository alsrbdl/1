n, m, k = map(int, input().split())
a = list(map(int, input().split()))
result = 0

a.sort()
f = a[n-1]
s = a[n-2]

count = int(m/(k+1)) * k
count += m%(k+1)

result += (count) * f
result += (m-count) * s

print(result)