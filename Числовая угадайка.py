import random
def is_valid(str, bordering=100):
    if str.isdigit() == True and 1<int(str) <= bordering:
        return True
    else:
        return False
randnum = random.randint(1, 101)
a = 'y'
while a != 'n':
    print('Добро пожаловать в числовую угадайку')
    border = input('Введите границу числа')
    border = int(border)
    count = 0
    while True:
        num = input(f'Введите число от 1 до{border}')
        count+=1
        if not is_valid(num, bordering=border):
            print('А может быть все таки введем число от 1 до', border,'?')
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

