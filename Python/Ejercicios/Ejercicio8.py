N = int(input())
if N > 5 and N < 2000:
  for i in range(2, N + 1, 2):
    POTENCIA = pow(i, 2)
    print(str(i) + '^2 = ' + str(POTENCIA))
    