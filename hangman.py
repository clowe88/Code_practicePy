hangman = "rollercoaster"
a_hangman = []
d_hangman = []
current_hangman = ""
guess_num = 0
hangman_len = len(hangman) - 1
limit = 20

for x in hangman:
    a_hangman.append(x)
    d_hangman.append("-")

print("You have " + str(limit) + " guesses to get the answer.") 

while guess_num < limit:
    guess = input("Guess a letter in the word: ")

    if guess == "quit":
        break

    incorrect = 0
    for x in a_hangman:
        if guess == x:
            d_hangman[incorrect] = x
        elif d_hangman[incorrect] != "-":
            d_hangman = d_hangman
        else:
            d_hangman[incorrect] = "-"
 
        incorrect += 1
    
    for x in d_hangman:
        current_hangman = current_hangman + x
       
        

    if current_hangman == hangman:
        print("You Win!!!")
        print (current_hangman)
        guess_num = 20
    else: 
        print("Keep Guessing")
        print (current_hangman)
        
    print (guess_num)   
    current_hangman = ""
    guess_num += 1

