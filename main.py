import random

print('вы играете в камень ножницы бумага с компом')
ways = ['камень', 'ножницы', 'бумага']
while(True):
    print('вводите')
    comp = random.randint(0,2)
    try:
        indx = ways.index(input())
        if comp - indx == -2:
            print("комп: " + ways[comp] + ", вы выиграли")
        elif comp - indx == 2:
            print("комп: " + ways[comp] + ", вы проиграли")
        elif comp - indx > 0:
            print("комп: " + ways[comp] + ", вы выиграли")
        elif comp - indx == 0:
            print("комп: " + ways[comp] + ", ничья")
        else:
            print("комп: " + ways[comp] + ", вы проиграли")
    except BaseException:
        print("нет такого слова")