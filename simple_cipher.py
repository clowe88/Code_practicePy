phrase = input("Enter a word or phrase to be encrypted: ")

phrase_arr = []
finished_phrase = ""

for i in phrase:
    phrase_arr.append(i)

for x in phrase_arr:
    num = ord(x)
    cipher = chr(num + 12)
    finished_phrase += cipher

print (finished_phrase)

