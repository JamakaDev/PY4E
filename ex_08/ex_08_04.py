fname = input("Enter a filename: ")
with open(fname) as file:
    fhand = file.read()
    words = fhand.split()
    lst = list()
    for word in words:
        if word not in lst:
            lst.append(word)
    lst.sort()
    print(lst)

