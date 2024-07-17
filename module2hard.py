n = int(input('Введите число от 3 до 20: '))
password = ''
for i in range(1, n):
    i = int(i)
    for j in range(i, n):
        if n % (i + j) == 0:
            password += str(i)+str(j)
print(f'{n} - '+password)




