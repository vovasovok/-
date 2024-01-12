import random
def is_valid(str):
    if str.isdigit() == True and 1<int(str)<=100:
        return True
    else:
        return False
randnum = random.randint(1, 101)
a = 'y'
while a != 'n':
    print('Добро пожаловать в числовую угадайку')
    count = 0
    while True:
        num = input('Введите число от 1 до 100''\n')
        count+=1
        if not is_valid(num):
            print('А может быть все таки введем число от 1 до 100?')
            continue
        num = int(num)
        if num<randnum:
            print('Ваше число меньше загаданного попробуйте еще разок')
            continue
        elif num> randnum:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif num == randnum:
            print('Вы угадали, поздравляем!')
            print('Использовано попыток', count)
            print('Спасибо что играли в числовую угадайку до свидания')
            a = input('Хотите ли сыграть еще? Если хотите введите y, если нет то n')
            break

