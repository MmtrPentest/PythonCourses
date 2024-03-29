# пример
s = set('МножествО один')
print(s)

# операции с множествами
s1 = set('Множество 1')
s2 = {'М', 'н', 'о', 'ж', 'е', 'с', 'т', 'в', '2', ' '}
print(s1 & s2) # {'е', 'о', ' ', 'ж', 'с', 'т', 'в', 'н', 'М'}
print(s1 - s2) # {'1'}
print(s1 | s2) # {'о', 'с', ' ', 'в', 'т', 'н', '1', 'М', 'е', '2', 'ж'}
print(s1 ^ s2) # {'1', '2'}


s1 = set('Множество 1')
# неизменяемое множество
s2 = frozenset('Множество 2')

s1.add('3')
print(s1) # {'н', 'ж', '1', 'М', ' ', 'е', '3', 'т', 'с', 'о', 'в'}
s2.add('3') # ERROR !!!
