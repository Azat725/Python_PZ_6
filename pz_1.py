num = int(input('Введите число: '))

a = len(str(num))

amount = 0

print('Количество символов в вашем числе: ', len(str(num)))

print(str(num).count('0'))

for i in (str(num)):
    amount += int(i)
print('Сумма цифр = ', amount)

print('Среднее арифметическое = ', amount // a)
