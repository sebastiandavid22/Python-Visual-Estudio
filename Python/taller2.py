A1= int(input())
A2= int(input())
A3= int(input())
op1 = A1*0 +A2*2 +A3*4
op2 = A1*2 +A2*0 +A3*2
op3 = A1*4 +A2*2 +A3*0
if(op1 <= op2):
    result = op1
elif(op2 <= op3):
    result = op1
else:
    result = op3
    
print(result)

