
class Matrix:
    def __init__(self, str1, str2, str3):
        self.str1 = str1
        self.str2 = str2
        self.str3 = str3
        self.mat = []


    def __add__(self, other):
       return Matrix(self.str1 + other.str1, self.str2 + other.str2, self.str3 + other.str3)


    def __str__(self):
        return f"{self.str1}\n{self.str2}\n{self.str3}"




mat_1 = Matrix([1, 2, 3], [4, 58, 8], [67, 24, 13])

mc_1 = Matrix(1, 2, 3)
mc_2 = Matrix(4, 58, 8)
mc_3 = Matrix(67, 24, 13)

print(mc_1 + mc_1, mc_2 + mc_2, mc_3 + mc_3)



