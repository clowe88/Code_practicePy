import random
a = []
over = []
under = []
odd = []
even = []
total_odd = 0
total_even = 0

for i in range(0,random.randrange(500)):
    a.append(i)

for i in a:
    if i <= len(a)/2:
        under.append(i)
    else:
        over.append(i)
    
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

for i in odd:
    total_odd += i
for i in even:
    total_even += i

print ("These numbers are over " + str(len(a)/2))
print(over)
print ("These numbers are under " + str(len(a)/2))
print(under)
print("These numbers are the odd number from 0 to " + str(len(a)))
print(odd)
print("These numbers are the even number from 0 to " + str(len(a)))
print(even)
print ("This is the total of the even numbers from 0 to " + str(len(a)))
print(total_even)
print ("This is the total of the odd numbers from 0 to " + str(len(a)))
print(total_odd)