#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Hello, world!'

pattern = '([\S]+)(,\s)([\S]+)!'

print(re.match(pattern,text))
print(re.match(pattern,text).group())
print(re.match(pattern,text).groups())
