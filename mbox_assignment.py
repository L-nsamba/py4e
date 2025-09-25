name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')

count_dict = dict()

for line in handle:
    if  line.startswith ('From '):
        strip = line.rstrip
        line = line.split()
        emails = line[1]
        #print(emails)
        count_dict[emails] = count_dict.get(emails, 0) + 1

big_count = None
big_user = None

for email, count in count_dict.items():
    if big_count is None or count > big_count:
        big_user = email
        big_count = count

print(big_user, big_count)