fname = input('Enter a filename: ')

with open(fname) as file:
    lst_1 = file.readlines()
    emails = list()
    count = 0
    for word in lst_1:
        if word.startswith('From '):
            count +=1
            emails = word.split()
            print(f'Email {count}: {emails[1]}')
    print('There were {} lines in the file with From as the first word'.format(count))
    print('As you can see {} emails were sent in this file'.format(count))
