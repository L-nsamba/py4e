count = dict()

user_input = input("Enter your sentence: ")
user_input = user_input.split()

print(f"""Your input is
{user_input}""")

for words in user_input:
    count[words] = count.get(words, 0) + 1
print(count)


