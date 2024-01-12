import random
def is_valid(str):
    if str.isdigit() == True and 1<int(str)<=100:
        return True
    else:
        return False
randnum = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку')
while True:
    num = input('Введите число от 1 до 100''\n')
    if not is_valid(num):
        print('А может быть все таки введем число от 1 до 100?')
        continue
    num = int(num)
    if num<randnum:
        print('')

