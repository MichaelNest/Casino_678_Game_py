from ctypes import  *

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

valuta ='грн.'
money = 0
startMoney = 0
defaultMoney = 10000
play_game = True

'''Установка цвета текста'''
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)


'''Функция ввода значения'''
def get_input(digit, messege):
    color(7)
    ret = ''
    while(ret == '' or not ret in digit):
        ret = input(messege)
    return ret


'''Функция ввода целого числа'''
def get_int_input(minimum, maximum, messege):
    color(7)
    ret = -1
    while(ret < minimum or ret > maximum ):
        st = input(messege)
        if(st.isdigit()):
            ret = int(st)
        else:
            print('    Enter your number!!')
    return ret

'''Вывод на экран цветного обрамленного текста'''
def color_line(c, st):
    for i in range(5):
        print()
    color(c)
    print('*'*(len(st)+2))
    print(' '+st)
    print('*' * (len(st) + 2))

'''Вывод сообщения о проигрыше'''
def peremoga(result):
    color(14)
    print(f'    Победа за тобой!! Выигрыш составил {result} {valuta}')
    print(f'    У тебя на счету {money}')

'''Вывод сообщения о проигрыше'''
def zrada(result):
    color(12)
    print(f'    К сожалению - проигрыш: {result} {valuta}')
    print(f'    У тебя на счету: {money}')
    print('    Обязательно нужно отыграться!!!')

'''Чтение из файла оставшейся суммы'''
def load_money():
    try:
        with open('money.dat', 'r') as fr:
            m = int(fr.readline())
    except FileNotFoundError:
        print(f'Файла не существует. Задано значение {defaultMoney} {valuta}')
        m = defaultMoney
    return m

'''Запись суммы в файл'''
def save_money(money_to_save):
    try:
        with open('money.txt', 'w') as fw:
            fw.write(str(money_to_save))
    except:
        print('Ошибка создания файла, наше Казино закрывается!!')
        quit(0)

'''ЗАПУСК ИГРЫ'''
def main():
    global money, play_game
    money = load_money()
    startMoney = money

    '''Главный цикл'''
    while(play_game and money>0):
        color_line(10, 'Приветствую тебя в нашем Казино, дрежище!!')
        color(14)
        print(f'У тебя на счету {money} {valuta}')

        color(6)
        print('  Ты можешь сыграть в: ')
        print('    1. Рулетку')
        print('    2. Кости')
        print('    3. Однорукого Бандита')
        print('    0. Выход. Ставка 0 в играх - выход')
        color(7)

        x = get_input('0 1 2 3 4', '    Твой выбор?    ')
        if(x=='0'):
            play_game = False
        elif(x =='1'):
            pass #roulette()
        elif(x =='2'):
            pass #dice
        elif(x == '3'):
            pass #one_hand_bandit()

    color_line(12, 'Жаль, что ты покидаеш нас! Но возвращайся скорей!!')
    color(13)
    if(money <=0):
        print('Упс. Ты остался без денег. Возьми микрокредит и возвращайся!!')

    color(11)
    if(money >startMoney):
        print('Ну чтож, поздравляем с прибылью')
        print(f'На начало игры у тебя было {startMoney} {valuta}')
        print(f'Сейчас уже {money} {valuta}! Играй еще и приумножай!!')
    else:
        print(f'К сожалению, ты проиграл {startMoney - money} {valuta}')
        print('В следующий раз все обязательно получится!!')
    save_money(money)

    color(7)
    quit(0)

if __name__ == '__main__':
    main()









# for i in range(16):
#     color(i)
#     print(f'Color is {i}')

# color_line(5, 'Hello!! It is I')

# a = get_int_input(0, 10, "Enter from 0 to 10:")
# print(a)

# print(f"You enter number {get_input('1 2', 'Enter 1 or 2 ')}")


