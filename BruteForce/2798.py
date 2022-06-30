n, m = input().split()
lst = list(map(int, input().split()))
value = []

n = int(n)
m = int(m)

for i in range(0, n-2): 
  for j in range(i+1, n-1): #focus on prior start point(i)
	  for k in range(j+1, n): #focus on prior start point(j)
            if (lst[i]+lst[j]+lst[k] <= m):
			          value.append(lst[i] + lst[j] + lst[k])
            
print(max(value))
