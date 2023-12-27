heigh = eval(input('Введите высоту ромба: '))
for i in range(heigh):
    print(' ' * (heigh - i), '$' * (2 * i + 1))
for i in range(heigh - 2, -1, -1):
    print(' ' * (heigh  - i), '$' * (2 * i + 1))