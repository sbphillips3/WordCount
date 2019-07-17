from collections import Counter

sentence = ('this is sample text with several words '
       'this is more sample text with some different stupid words'
       'So you can wipe off that grin')

cnter = Counter(sentence.split())

for word, count in sorted(cnter.items()):
    print(f'{word:<15}{count}')

