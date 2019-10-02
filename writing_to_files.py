# "r+" makes the file readable. "w+" makes the file writable, and "a+" makes the file appendable.
file = open("C:\/Users\/chris88\/Documents\/Code Practice\/test.csv", "a+")
# \r\n moves to a new line.
file.write("This is how you open and write to a file \r\n")
contents = file.read()

print(contents)
file.close()