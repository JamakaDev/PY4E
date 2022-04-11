import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
import ssl

#Ignore the SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

#Open URL
# url = input('Enter URL: ')
# data =  urllib.request.urlopen(url)
# data = data.read()

#Parse through XML with ElementTree
# tree = ET.fromstring(data)
# lst = tree.findall('comments/comment')
# count_lst = sum([int(i.find('count').text) for i in lst])
# print(count_lst)

#Parse through JSON with json
# data_dic = json.loads(data)
# count = sum([data_dic['comments'][i]['count'] for i in range(len(data_dic['comments']))])
# print(count)
#--------------------------------------------------------------------------------


