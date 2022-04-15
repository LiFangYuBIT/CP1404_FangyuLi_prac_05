"""this is a collection of words of nice words this is a fun thing it is"""

word_list = {}
text = input("Text: ")
words = text.split()
max_length = max((len(word) for word in words))

for word in words:
    times = word_list.get(word, 0)
    word_list[word] = times + 1

words = list(word_list.keys())
words.sort()

for word in words:
    print(f"{word:<{max_length}} : {word_list[word]}")
    print("{:{}} = {}".format(word, max_length, word_list[word]))
