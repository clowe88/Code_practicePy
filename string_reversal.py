a = ("This is a reverse string.")
b = []
c = ("")
i = len(b)-1
for x in a:
    b.append(x)

for x in b:
    c = c + b[i]
    i -= 1
    

print(b)
print(c)