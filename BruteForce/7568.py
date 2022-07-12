num = input()
num = int(num)
list = []
weight = []
height = []
order = []
for i in range(num):
  list.extend(map(int, input().split())) //transform string input into int

for j in range(num):
  weight.append(list[j*2])
  height.append(list[j*2+1])

for m in range(num): 
  count = 1
  for n in range(num):
    if(weight[n] > weight[m] and height[n] > height[m]):
      count = count + 1
  order.append(count)
  print(count, end=" ")
  
 
//When the list is empty, it is impossible to insert the element with index 2 or others
