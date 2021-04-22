# this is create an new file with name text.txt or open that file name.
file = open('text.txt', 'w')
# this will overwrite
file.write("This is title of file\n")
file.close()


# this add new line in file
file = open('text.txt', 'a')
for i in range(1,30+1):
    file.write(f"This is {i} line number in text.txt\n")
file.close()


# reading the file data
file = open('text.txt', 'r')
readlines = file.readlines()
for i in range(len(readlines)):
    print(f'line number {i+1}: {readlines[i]}')