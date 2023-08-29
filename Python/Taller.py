
a, b = input().split()
s = str(b)
Pestaña= int(a)
for i in range(0, int(b)):
    if s[i] == "fechou":
        Pestaña += 1
    elif s[i] == "clicou":
        Pestaña -= 1
print(Pestaña)