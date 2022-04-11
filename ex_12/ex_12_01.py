#Ex_01/Ex_02
import urllib.request, urllib.parse, urllib.error
# import socket
# try:
#     url = input("Enter a URL/website: ")
#     host = url.split('/')
#     host = host[0]
#     port = 80
#
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect((host,port))
#     cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
#     mysock.send(cmd)
#
#     char_count = {}
#     chars_len = 0
#     while True:
#         data = mysock.recv(512)
#         #print(len(data))
#         if len(data) < 1:
#             break
#         chars = data.decode()
#         chars_len+=len(chars)
#         for char in chars:
#             char_count[char] = char_count.get(char, 0)+1
#         if chars_len  < 3000:
#             print(chars, chars_len)#, '*******************',len(chars),'*******************')
#
#     char_sort = [(v,k) for k,v in char_count.items()]
#     char_sort.sort(reverse=True)
#     char_sort = [(k,v) for v,k in char_sort]
#     char_count = dict(char_sort)
#
#     print(char_count)
#
#
#     mysock.close()
# except:
#    print('Error please try again')

#Ex_03
# import urllib.request, urllib.error

# url = input("Enter a URL/website: ")
# page = urllib.request.urlopen(f'http://{url}')
#
# lines_count = 0
# for lines in page:
#     lines = lines.decode().rstrip()
#     lines_count += len(lines)
#     if lines_count <= 3000:
#         print(lines)
# print(lines_count)


#Ex_04
# import urllib.request
# count = 0
# url = input('Enter URL: ')
# page = urllib.request.urlopen(f'http://{url}')
# for i, lines in enumerate(page):
#     lines = lines.decode().strip()
#     if lines.startswith('<p'):
#         count+=1
# print(f'There are {count} paired paragraph tags or {count*2} total paragraph tags!')

# #Ex_05
# import socket
#
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/mbox-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# data_lines = ''
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1: break
#     data_lines += data.decode()
#     if len(data_lines) >= 3000: break
#
# file = data_lines.split('\r\n\r\n')
# file_header = file[0]
# file_content = file[1]
# for line in file_content.split('\n'):
#     if line.startswith('Received'):
#         print(line.split()[2])
# print('*'*50)
# print(file_content)


