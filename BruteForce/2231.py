#BruteForce - 분해합(decompose sum)

n = int(input())
result  = 0
             
for i in range(n+1):
  digit = list(map(int, str(i))) #build a list with integer nums
  if(sum(digit) + i == n):
      result = i
      break
print(result)
