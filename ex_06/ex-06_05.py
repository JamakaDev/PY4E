text = "X-DSPAM-Confidence:    0.8475"
start = text.find(':')
num = float(text[start+1:])
print(num)

for i in text:
    if i != i[0]:
        print('Nope')
