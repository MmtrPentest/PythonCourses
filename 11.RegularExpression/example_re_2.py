#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = "Hello. Меня зовут Вася и мне 15 лет"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = "Hello. Меня зовут Вася и мне 15 лет"

pattern = r'\d+'
print(re.findall(pattern, text)) # ['15']
pattern = r'^\D'
print(re.findall(pattern, text)) # ['H']
pattern = r'[\d\D]+'
print(re.findall(pattern, text)) #
pattern = r'[\s\S]+'
print(re.findall(pattern, text)) # ['зовут Вася ']
pattern = r'зовут\s([А-я]+)\s'
print(re.findall(pattern, text)) # ['Вася']

pattern = r'[^\w]'
print(re.findall(pattern, text))
