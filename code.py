import string
import sys

# This function reads a file and returns how many times each word appears

def read_words(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read().lower()
    except FileNotFoundError:
        print(f"ERROR!! FILE NOT FOUND: {filename}")
        return {}

    #Removing punctuation and splitting the text into words
    text = ''.join(c for c in text if c not in string.punctuation)
    words = text.split()

    #Word counts
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict

#Opening both essays
print("Opening Essay 1:")
essay1_wordlist = read_words('essay1.txt')

print("Opening Essay 2:")
essay2_wordlist = read_words('essay2.txt')

if not essay1_wordlist or not essay2_wordlist:
    print("Oops! Need both essays to proceed.")
    sys.exit()

#Finding words both essays share
similar_words = set(essay1_wordlist) & set(essay2_wordlist)

#The given menu options

def word_query():
    while True:
        print("\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
        print("Menu Options")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
        print("1. Display similar words")
        print("2. Find a specific word")
        print("3. Compute plagiarism")
        print("4. Exit")
        print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")

        choice = input("Choose an  option [1-4]: ")

        if choice == "1":
            print("\nSIMILAR WORDS IN THE ESSAYS:\n")
            for word in sorted(similar_words):
                print(f"{word}:\n Essay 1: {essay1_wordlist[word]} times\nEssay 2: {essay2_wordlist[word]} times\n")

        elif choice == "2":
            search = input("Enter the word you want to search: ").lower().strip(string.punctuation)
            e1 = essay1_wordlist.get(search, 0)
            e2 = essay2_wordlist.get(search, 0)
            if e1 == 0 and e2 == 0:
                print(f"'{search}' not found in both essays.")
            else:
                print(f"'{search}' found:")
                print(f" Essay 1: {e1} times")
                print(f" Essay 2: {e2} times")

        elif choice == "3":
            union_words = set(essay1_wordlist) | set(essay2_wordlist)
            if len(union_words) == 0:
                print("Plagiarism Rate: 0% (no words to compare)")
            else:
                score = (len(similar_words) / len(union_words)) * 100
                score = round(score, 2)
                print(f"\nPlagiarism Rate: {score}%")
                if score >= 50:
                    print("ALERT!!! Possible Plagiarism detected.")
                else:
                    print("CONGRATULATIONS!!! Plagiarism check passed.")

        elif choice == "4":
            print("Exiting the program have a nice day.....")
            break

        else:
            print("Oops!! Please enter a number between 1 and 4.")

#Looping through the menu options

word_query()