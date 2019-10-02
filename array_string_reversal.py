a = [" This", " is", "a ", "reverse ", "string ", "array "]
b = []
c = ""
d = ""
for x in a:
    c = ""
    for z in x:
        c = z+c
    b.append(c)

for x in b:
    d = d+x

print (d)