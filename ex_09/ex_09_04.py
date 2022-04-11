name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
fhand = handle.read()
fhand = fhand.splitlines()
email = dict()
for lines in fhand:
    if lines.startswith('From '):
        lines = lines.split()
        email[lines[1]] = email.get(lines[1],0)+1
max_emails = ''
count = 0
for k,v in email.items():
    if email[k] > count:
        max_emails = f'{k} {v}'
        count = email[k]
print(max_emails)
handle.close()
