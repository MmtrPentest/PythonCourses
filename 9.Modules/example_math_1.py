#!/usr/bin/python
# -*- coding: utf-8 -*-

from figures import square

print(square.area(5))

from figures import circle

print(circle.len(10))

from figures.rectangle import area

print(area(5,10))