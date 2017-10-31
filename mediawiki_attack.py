import requests
client = requests.session()
l3url = "http://10.129.26.121/mediawiki/api.php?action=query&meta=tokens"
l3 = client.post(l3url)
article_token = l3.text[4241:4283]
print(l3.text)
print(article_token)
title = input("Article title:")
summary = input("Article Summary:")
content = input("Article Content:")
l4url = "http://10.129.26.121/mediawiki/api.php?action=edit"
article_data = {'token':article_token, 'title':title,'summary':summary,'text':content }
l4 = client.post(l4url,data=article_data)
