'''
не работает
'''
import re

url = 'http://bigazzzz.ru/login.php?login=user&password=123456&submit=true'

pattern = r'.+\?([\S]+&?)+'
print(re.findall(pattern,url))

