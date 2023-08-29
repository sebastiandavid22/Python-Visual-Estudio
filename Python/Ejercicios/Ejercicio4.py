X, Y = input().split()
X - int(X)
Y= int(Y)
if X == 1:
 TOTAL = Y * 4.0
elif X == 2:
 TOTAL = Y * 4.5
elif X == 3:
 TOTAL = Y * 5.0
elif X == 4:
 TOTAL = Y * 2.0
elif X == 5:
 TOTAL = Y * 1.5
print('Total: R$ %.2f' %TOTAL)
