class A:
    def func(self, i):
        return i * i

    def digui(self, i):
        if i == 1:
            return 1
        return self.func(i) + self.digui(i - 1)


print(type(A().digui(3)))