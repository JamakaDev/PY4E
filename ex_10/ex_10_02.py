fname = input('Enter filename: ')
if len(fname) < 1:
    handle = open('mbox-short.txt')
else:
    handle = open(fname)
email_hours = dict()

for lines in handle:
    lines = lines.rstrip()
    if lines.startswith('From '):
        lines = lines.split()
        for line in lines:
            if ':' in line:
                hour = line.split(':')
                hour = hour[0]
                if hour not in email_hours:
                    email_hours[hour] = 1
                else:
                    email_hours[hour] +=1
for k,v in sorted([(k,v) for k,v in email_hours.items()]): print(k, v)


