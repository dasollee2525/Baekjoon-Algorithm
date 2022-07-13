length, width = input().split()
length = int(length)
width = int(width)

board = []
color = []


for i in range(length):
  board.append(list(input()))

for i in range(length-7):
  for j in range(width-7):
    count_case1 = 0
    count_case2 = 0
    for n in range(i, i+8):
      for m in range(j, j+8):
        if (m+n) % 2 == 0:
          if(board[n][m] == 'B'):
            count_case1 += 1
          if(board[n][m] == 'W'):
            count_case2 += 1
        else:
          if(board[n][m] == 'W'):
            count_case1 += 1
          if(board[n][m] == 'B'):
            count_case2 += 1
    color.append(count_case1 if count_case1 < count_case2 else count_case2)

print(min(color))

//Determine the number of index correctly and carefully
