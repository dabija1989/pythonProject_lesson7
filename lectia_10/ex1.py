"""
    Ask the user to input a large text with many words. Ignoring punctuation.
    Calculate how many times each word (regardless the case) was used.

Hints: Use str.split(' ') to break down the text into a list

Example:
Input:
how much wood would a woodchuck chuck if a woodchuck could chuck wood
Output:
Word "how" was used 1 times.
Word "much" was used 1 times.
Word "wood" was used 2 times.
Word "would" was used 1 times.
Word "a" was used 2 times.
Word "woodchuck" was used 2 times.
Word "chuck" was used 2 times.
Word "if" was used 1 times.
Word "could" was used 1 times.
"""
# Solution

import string

# Get input from the user
text = input("Enter a large text: ")
words = text.lower().split(' ')
word_counts = []

for word in words:
    word = word.strip(string.punctuation + string.digits) #verificam punctuatia dupa fiecare cuvant si oeliminam daca exista
    found = False
    for count in word_counts:
        if count[0] == word: #comparam elementele din lista words cu primul element din lista [word,1]creata la fiecare noua iteratie
            count[1] += 1 #daca primele elemente sunt egale incrementam al doilea element cu 1
            found = True #cand found este true se neaga conditia si astfel elementul nu se adauga in lista
    if not found:
        word_counts.append([word, 1])
#print(word_counts)
for count in word_counts:
    print(f'Word "{count[0]}" was used {count[1]} times.')
# solution 2

text = input("Enter a large text: ")
words = text.lower().split(' ')
word_counts = {}

for word in words:
    word = word.strip(string.punctuation + string.digits)
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    print(f'Word "{word}" was used {count} times.')