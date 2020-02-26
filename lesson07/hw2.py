class Clothes:


    def __call__(self, size=None, height=None):
        print(f'Потрачено ткани на пальто {size / 6.5 + 0.5}')
        print(f'Потрачено ткани на костюм {height * 2 + 0.3}')
        print(f'Потрачено общее количество ткани {(size / 6.5 + 0.5) + (height * 2 + 0.3)}')

clothes = Clothes()
clothes(5, 5)








