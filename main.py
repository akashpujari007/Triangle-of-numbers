n = int(input())
i = 1
while i <= n:
  spaces = 1
  while spaces <= n - i:
    print(' ', end ='')
    spaces = spaces + 1
  p = i
  j = 1
  while j <= i:
    print(p, end='')
    j = j + 1
    p = p + 1
  p = (2 * i) - 2
  while p > i - 1:
    print(p, end='')
    p = p - 1
    j = j + 1
  print()
  i = i + 1