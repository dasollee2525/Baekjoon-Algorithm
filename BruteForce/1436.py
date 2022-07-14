N = int(input())

num = 666
count = 0

while(count < N-1):
  num += 1
  str_num = str(num)
  if "666" in str_num:
    count += 1

print(num)
