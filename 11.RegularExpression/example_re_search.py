#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

text = 'Hello, world!'
pattern = '(?i:h)ello(?#туткомментарий)'
print(re.search(pattern,text).group())
pattern = '(?i)hello(?#туткомментарий), (world)!'
print(re.search(pattern,text).groups())
print(re.search(pattern,text).group(1))

