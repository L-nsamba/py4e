name = input("Enter a file name: ")

if len(name) < 1:
    name = 'essay1.txt'

fhand = open('essay1.txt', 'r')
word_counter = dict()

for lines in fhand:
    lines = lines.rstrip()
    words = lines.split()
    #print(words)
    for characters in words:
        #print(characters)
        word_counter[characters] = word_counter.get(characters, 0) + 1
        #print(characters)

for word, count in word_counter.items():
    print(word, count)