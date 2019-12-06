from ctypes import  *


windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

valuta ='грн.'
defaultMoney = 10000

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
    for i in range(30):
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
        with open('money.dat', 'w') as fw:
            fw.write(str(money_to_save))
    except:
        print('Ошибка создания файла, наше Казино закрывается!!')
        quit(0)



for i in range(16):
    color(i)
    print(f'Color is {i}')

# color_line(5, 'Hello!! It is I')

# a = get_int_input(0, 10, "Enter from 0 to 10:")
# print(a)

# print(f"You enter number {get_input('1 2', 'Enter 1 or 2 ')}")

# def main():
#     pass
#
# if __name__ == '__main__':
#     main()
