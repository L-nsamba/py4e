
import re
fhand = open('regex_sum_2243225.txt', 'r')
total = 0

for lines in fhand:
    lines = lines.rstrip()
    numbers = re.findall('[0-9]+', lines)
    if numbers:
        for num in numbers:
            num = int(num)
            total = total + num

print(total)