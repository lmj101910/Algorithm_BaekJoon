check = 'wrong'

while(True):
  triangle = list(map(int, input().split()))

  x = min(triangle)
  triangle.remove(x)
  y = min(triangle)
  triangle.remove(y)
  z = min(triangle)
  triangle.remove(z)
  
  if x == 0 and y == 0 and z == 0:
    break

  if z ** 2 == (x ** 2) + (y ** 2):
    check = 'right'
  else:
    check = 'wrong'

  print(check)
  
