num = int(input())
array = []
count = 0

def push(obj, count):
  array.append(obj)
  count = count + 1
  return count

def pop(count):
  if count == 0:
    return -1
  else:
    count = count -1
    return array.pop(count)

def size():
  return len(array)

def empty():
  if count == 0:
    return 1
  else:
    return 0

def top():
  if count == 0:
    return -1
  else:
    return array[count] 
  

for i in range(num):
  command = input()
  result = ''
  if command.find("push") != -1:
    str, num = command.split()
    num = int(num)
    count = push(num, count)
  elif command == 'pop':
    result = pop(count)
    print(result)
  elif command == 'size':
    result = size()
    print(result)
  elif command == 'empty':
    result = empty()
    print(result)
  elif command == 'top':
    result = top()
    print(result)
