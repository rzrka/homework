import random
class Loto:
    def __init__(self):
        self.end = None
        self.counter = 90
        self.string_player = []
        self.string_PC = []
        self.barrel = str(random.randint(0, 100))

    def make_loto_player(self):
        no_dooble = 2
        while no_dooble >= 2:
            check_list = []
            for x in range(3):
                res = [' ' + str(random.randint(0, 100)) for _ in range(5)] + list('   ' * 4)
                random.shuffle(res)
                self.string_player.append(res)
                check_list.extend(res)
            for i in range(100):
                no_dooble = check_list.count(' ' + str(i))
                if no_dooble >= 2:
                    self.string_player.clear()
                    check_list.clear()
                    break

    def make_loto_PC(self):
        no_dooble = 2
        while no_dooble >= 2:
            check_list = []
            for x in range(3):
                res = [' ' + str(random.randint(0, 100)) for _ in range(5)] + list('   ' * 4)
                random.shuffle(res)
                self.string_PC.append(res)
                check_list.extend(res)
            for i in range(100):
                no_dooble = check_list.count(' ' + str(i))
                if no_dooble >= 2:
                    self.string_player.clear()
                    check_list.clear()
                    break

    def show_loto(self):
        self.barrel = str(random.randint(0, 100))
        print('Новый бочонок: ' + self.barrel + ' осталось боченков: ' + str(
            self.counter) + '\n' + '---- Ваша карточка ----')
        for x in self.string_player:
            print(''.join(x))
        print('---- Карточка компьютера ----')
        for x in self.string_PC:
            print(''.join(x))
        user = input('Зачеркнуть цифру? (y/n) ')
        if user == 'n':
            answer = ' ' + self.barrel
            for i in self.string_player:
                for j in i:
                    if j == answer:
                        self.end = 'поражение'
        elif user == 'y':
            my_check = None
            answer = ' ' + self.barrel
            for i in self.string_player:
                for j in i:
                    if answer == j:
                        k = i.index(answer)
                        i[k] = '-'
                        my_check = 1
            if my_check == None:
                self.end = 'поражение'
        else:
            print('Вы ввели не то значение')
        for i in self.string_PC:
            for j in i:
                if ' ' + self.barrel == j:
                    k = i.index(' ' + self.barrel)
                    i[k] = '-'
        self.counter -= 1

loto = Loto()
loto.make_loto_player()
loto.make_loto_PC()
while loto.end != 'поражение':
    loto.show_loto()
    if loto.end == 'поражение' or loto.counter == 0:
        print('Вы проиграли')










































































