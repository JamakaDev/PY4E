file = input('Enter a filename: ')
handle = open(file)
hand = handle.read()
hand = hand.split()
sample = dict()
for words in hand:
    if words not in sample:
        sample[words] = len(words)
print(sample)
handle.close()


