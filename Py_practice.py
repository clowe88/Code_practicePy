def activity01(num1):
    if num1%2 == 0: print("Even") 
    else: print("odd")

def activity02(iv_one, iv_two):
    total = iv_one + iv_two
    print(total)

def activity03(num_list):
    x = 0
    for i in num_list:
        if i%2 == 0:
            x += 1
    print (x)

def activity04(input_string):
    print (input_string[::-1])

activity04("ghost")