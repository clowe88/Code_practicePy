def collatz():
    startnum = int(input("Enter a number to test the Collatz Theory: "))
    highnum = 0
    finalnum = startnum
    numlist = []
    i = 0

    

    while finalnum != 1:
        if finalnum % 2 == 0:
            finalnum = (finalnum/2)
        else:
            finalnum = (finalnum*3)+1
        
        if finalnum < highnum: 
            highnum = highnum
        else: 
            highnum = finalnum
        
        numlist.append(finalnum)
        i += 1

    print ("The number of times calculated: " + str(len(numlist)))
    print ("The highest number hit was: " + str(highnum))
    print ("We started with: " + str(startnum))
    print ("The final number was : " + str(finalnum))

collatz()

