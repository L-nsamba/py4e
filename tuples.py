name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        #print(time)
        hours = (time[0:2])
        #print(hours)
        count[hours] = count.get(hours, 0) + 1

#for t in sorted(count):
    #print(t, count[t])
    
tup_list = list()
for v,k in count.items():
    new_tup = (v, k)
    tup_list.append(new_tup)

sort_values = sorted(tup_list)

for k,v in sort_values:
    print(k, v)