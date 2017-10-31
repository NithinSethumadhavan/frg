import getpass
import requests

uname = input("Name:")
password = getpass.getpass("Password:")
l1url = "http://10.129.26.121/mediawiki/api.php?action=login&lgname=%s" % uname
print(l1url)
client = requests.session()
l1 = client.post(l1url)
a = l1.text
csrftoken = a[4344:4386]
print(csrftoken)
login_data = {'authAction' : 'login', 'force' : '', 'title' : "Special:UserLogin" , 'wpEditToken' : '+\\', 'wpLoginToken' : csrftoken , 'wpName' : uname, 'wpPassword' : password , 'wploginattempt' : 'Log in' }
l2url = "http://10.129.26.121/mediawiki/index.php?title=Special:UserLogin"
l2 = client.post(l2url,data=login_data)
l3url = "http://10.129.26.121/mediawiki/api.php?action=query&meta=tokens"
l3 = client.post(l3url)
article_token = l3.text[4241:4283]
print(article_token)
title = input("Article title:")
summary = input("Article Summary:")
content = input("Article Content:")
l4url = "http://10.129.26.121/mediawiki/api.php?action=edit"
article_data = {'token':article_token, 'title':title,'summary':summary,'text':content }
l4 = client.post(l4url,data=article_data)
