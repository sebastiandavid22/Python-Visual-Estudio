NUM1, NUM2 = input().split()
NUM1 = int(NUM1)
NUM2 = int (NUM2)
if NUM1 % NUM2 == 0 or NUM2 % NUM1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
