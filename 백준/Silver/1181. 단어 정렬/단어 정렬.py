n = int(input())
words = set()

for _ in range(n):
    words.add(input())

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)