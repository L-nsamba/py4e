"""fname = input("Enter file name: ")
fh = open('mbox-short.txt')
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    count = float(count)
    
    line = line.rstrip()
    sline = line.find('0.')
    fsline = line[sline:]
    fsline = float(fsline)
    total = total + fsline
    
average = total / count
print(f"Average spam confidence: {average}")"""


"""fname = input("Enter file name: ")
fh = open('romeo.txt', 'r')
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)"""



fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open('mbox-short.txt','r')
count = 0
email_list = list()

for line in fh:
    if line.startswith('From'):
        words = line.split()
        sentence = words[1:]
        if len(sentence) >= 6:
            email = sentence[0]
            print(email)
            count = count + 1

print("There were", count, "lines in the file with From as the first word")
