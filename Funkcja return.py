# def funkcjaZwyczajna(x):
#        return x+1
#
# def funkcjaDoFunkcji(f,x):
#        return f(x)
#
# print(funkcjaDoFunkcji(funkcjaZwyczajna, 2))
# print(dir(3))
#
#
# def funkcjaZewn(x):
#         def funkcjaWewn(y):
#             return x*y
#         return funkcjaWewn
# f = funkcjaZewn(-3.00)
# print(f)
#
# def funkcjaDoFunkcjiZewn(f):
#         def funkcjaWewn(x):
#             print("Tutaj funkcja wewnetrzna")
#             wynik = f(x)
#             return wynik+1
#         return funkcjaWewn
#
#
# f = funkcjaDoFunkcjiZewn(funkcjaZwyczajna)
# print(f(2))
# funkcjaZwyczajna = funkcjaDoFunkcjiZewn(funkcjaZwyczajna())

def dekoratorek(f):
    def funkcjaWewn(x):
        print("Tutaj funkcja wewnętrzna")
        wynik = f(x)
        return wynik+1
    return funkcjaWewn


@dekoratorek
def funkcjaZwyczajna(x):
    return x+1

print(funkcjaZwyczajna(2))
