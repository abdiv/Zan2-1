def my_func(a, b):
    c = set(a)
    d = set(b)
    print(c.intersection(d))
    if c == d:
       print('Слова состоят из одинаковых букв')



my_func('приипир', 'пирр')
