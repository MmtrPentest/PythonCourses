import requests
url = input('url=>')
r = requests.get(url)
htmlfile = open('site.html','w+', encoding=r.encoding)
htmlfile.write(r.text)
htmlfile.close()
