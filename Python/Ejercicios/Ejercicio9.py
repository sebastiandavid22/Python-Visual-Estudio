N= int(input())
for i in range(N):
  X, Y= map(int,input().split())
  if Y != 0:
      DIV = X/Y
      print('%.1f' %DIV)
  else:
   print('divisao impossivel')