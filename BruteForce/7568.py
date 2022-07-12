num = input()
num = int(num)
list = []
weight = []
height = []
order = []
for i in range(num):
  list.extend(map(int, input().split()))

for j in range(num):
  weight.append(list[j*2])
  height.append(list[j*2+1])

while(weight):
  max_weight = max(weight)
  max_height = max(height)
  if weight.index(max_weight) == height.index(max_height):
    
    if(weight.count(max(weight)) > 1 and height.count(max(height)) > 1):
  
