from ctypes import  *
import time
import random

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
        with open('money.txt', 'r') as fr:
            m = int(fr.readline())
    except FileNotFoundError:
        print(f'Файла не существует. Задано значение {defaultMoney} {valuta}')
        m = defaultMoney
    return m

'''Запись суммы в файл'''
def save_money(money_to_save):
    try:
        # fw = open('money.txt', 'w', encoding='utf-8')
        # fw.write(str(money_to_save))
        # fw.close()
        with open('money.txt', 'w') as fw:
            fw.write(str(money_to_save))
    except:
        print('Ошибка создания файла, наше Казино закрывается!!')
        quit(0)




'''Начало РУЛЕТКИ '''
def roulette():
    global money
    '''Маркер главного цикла метода Рулетка'''
    play_game = True

    '''Главный цикл рулетки '''
    while(play_game and money >0):
        '''Вывод меню игры '''
        color_line(3, 'ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!!')
        color(14)
        print(f'\n У тебя на счету {money} {valuta}\n')
        color(11)
        print('  Ставлю на...')
        print('       1. Нечетное (выигрыш 1:1)')
        print('       2. Четное (выигрыш 1:1)')
        print('       3. Дюжина (выигрыш 3:1)')
        print('       4. Число (выигрыш 36:1)')
        print('       0. Возврат в предыдущее меню')

        '''Ввод значения: выбор пункта меню'''
        x = get_input('0 1 2 3 4', 'Твой выбор:    ')

        play_roulette = True

        if(x == '3'):
            color(2)
            print()
            print('   Выбери числа: ...')
            print('       1. От 1 до 12')
            print('       2. От 13 до 24')
            print('       3. От 25 до 36')
            print('       0. Назад ')

            '''Выбор пункта меню дюжины'''
            duzhina = get_input('0  1 2 3', '    Твой выбор:    ')
            if(duzhina == '1'):
                text_duzhina = 'от 0 до 12'
            elif(duzhina == '2'):
                text_duzhina = 'от 13 до 24'
            elif(duzhina == '3'):
                text_duzhina = 'от 25 до 36'
            elif(duzhina == '0'):
                play_roulette = False
        elif(x == '4'):
            chislo = get_int_input(0, 36, '    На какое число ставиш (0..36): ')
        color(7)
        if(x == '0'):
            return 0
        if (play_roulette):
            stavka = get_int_input(0, money, f'    Сколько поставишь?? (не больше {money}):    ')
            if(stavka == 0):
                return 0
            number = get_roulette(True)
            print()
            color(11)
            print(f'    Выпало число {number}! '+ '*'*number)

            if(x == '2'):
                print('    Ты ставил на ЧЕТНОЕ!!')
                if(number < 37 and number % 2 == 0):
                    money += stavka
                    peremoga(stavka)
                else:
                    money -= stavka
                    zrada(stavka)
            elif(x == '1'):
                print('    Ты ставил на НЕЧЕТНОЕ!!')
                if(number < 37 and number % 2 !=0):
                    money += stavka
                    peremoga(stavka)
                else:
                    money -= stavka
                    zrada(stavka)
            elif(x == '3'):
                print(f'    Ставка зделана на диапазон чисел {text_duzhina}')
                win_duzhina = ''
                if(number < 13):
                    win_duzhina = '1'
                elif(number > 12 and number <25):
                    win_duzhina = '2'
                elif(number > 24):
                    win_duzhina = '3'
                if(duzhina == win_duzhina):
                    money += stavka*2
                    peremoga(stavka*3)
                else:
                    money -= stavka
                    zrada(stavka)

            elif(x == '4'):
                print(f'    Ставка сделана на число {chislo}')
                if(number == chislo):
                    money += stavka*35
                    peremoga(stavka*36)
                else:
                    money -= stavka
                    zrada(stavka)

            print()
            input('  Нажми Enter для продолжения...')

def get_roulette(visible):
    tick_time = random.randint(100, 200)/10000
    main_time = 0
    number = random.randint(0, 38)
    increase_tick_time = random.randint(100, 110)/100
    col = 1

    while(main_time < 0.7):
        col += 1
        if (col > 15):
            col = 1

        main_time += tick_time
        tick_time *= increase_tick_time

        color(col)
        number +=1
        if(number > 38):
            number = 0
            print()
        print_number = number
        if(number == 37):
            print_number = '00'
        elif(number == 38):
            print_number = '000'
        print('Число >', print_number, '*'*number, ' '*(79 - number*2), '*'*number)
        if(visible):
            time.sleep(main_time)
    return number



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

        x = get_input('0 1 2 3 4', '    Твой выбор:    ')
        if(x=='0'):
            play_game = False
        elif(x =='1'):
            roulette()
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


