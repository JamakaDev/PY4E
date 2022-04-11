fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO - You have been punk\'d')
        quit()
    else:
        print(f'The file "{fname}" does not exist!')
        quit()
total = 0
count = 0
for line in fhand:
    end = line.find(':')
    if line.startswith('X-DSPAM-Confidence:'):
        count+=1
        total += float(line[end+1:])
try:
    print(f'Average spam confidence: {total/count:.12}')
except:
    print('This did not show up in this file')
#count = 0
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         count +=1
#         print(count, line)
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     else:
#         count+=1
#         user_index = line.find(' ')
#         line = line.split('@')
#         user = line[0][user_index:]
#         host = line[1]
#         print(str(count)+'. '+user+'@'+host)
# with open('mbox-short.txt') as fhand:
#     for line in fhand:
#         line = line.strip()
#         if line.startswith('From:'):
#             print(line.upper())
#
