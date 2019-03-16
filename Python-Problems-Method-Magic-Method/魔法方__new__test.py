class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        print('1', str.__new__(cls, string))
        print('2', id(string.__new__(cls, string)))
        print('3', id(cls))
        print('4',id(str.__new__(cls, string)))
        return str.__new__(cls, string)


class test(CapStr):
    def __new__(cls, string):
        string = string.upper()
        return CapStr.__new__(cls, string)

a = CapStr("hello")
a.__new__(str, '===========')
print(issubclass(CapStr, str))
print(a)
# print(type(a))
# print(type(str))
# print(CapStr.__dict__)
# t = test("hello")



