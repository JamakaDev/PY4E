from urllib.request import urlopen
from bs4 import BeautifulSoup
import socket

# #Lab 1 Request/Response Cycle
# url = input("Enter a URL/website: ")
# host = url.split('/')
# host = host[0]
# port = 80
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((host,port))
# cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

#Lab 2

# html = urlopen('http://py4e-data.dr-chuck.net/comments_1439418.html').read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('span')
# span_sum = sum([int(tag.contents[0]) for tag in tags])
# print(span_sum)
# print('*'*50)
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)




# #Lab 3 Following Links w/ BeautifulSoup
# try:
#     url = input('Enter URL/website: ')
#     count = int(input('Enter count: '))
#     pos = int(input('Enter position: '))
#     html = urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     # for tag in tags:
#     #     print(tag.get('href',None))
#     while count > 0 :
#         tags = soup('a')
#         name = tags[pos-1].contents[0]
#         html = urlopen(f'http://py4e-data.dr-chuck.net/known_by_{name}.html').read()
#         soup = BeautifulSoup(html, 'html.parser')
#         count -=1
#     print(name)
#
# except ValueError:
#     print('Sorry that site is unknown or no longer available, try again')


