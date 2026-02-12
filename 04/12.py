class A:
    def hello(self) -> str:
        print('Hello')

    def __str__(self) -> str:
        return 'A.__str__ method'


class B:
    def good_evening(self):
        print('Good evening')

    def __str__(self) -> str:
        return 'B.__str__ method'


class C(A, B):
    pass


class D(B, A):
    pass

c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)

def new_method(arg):
    return  "new method"

def new_method2(arg):
    return "new method 2"


A.__str__ = new_method
B.__str__ = new_method2
c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(isinstance(c, A), isinstance(c, B))
print(isinstance(d, A), isinstance(d, B))
print(c)
print(d)