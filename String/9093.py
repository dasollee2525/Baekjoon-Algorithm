num = int(input())

def reverse(word):
  return word[::-1]

for i in range(num):
  sentence = input()
  word_list = sentence.split()
  re_list = list(map(reverse, word_list))
  result = ' '.join(s for s in re_list)
  print(result)
