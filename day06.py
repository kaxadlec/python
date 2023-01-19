## 전역변수, 지역변수
g = 1  # global variable

def print_global():
    print(g)

print(g)
print_global()

def print_global():
    g = 1  # local variable
    print(g)

print(g)
print_global()

g=2
def print_global():
    print(g)

def change_print_global():
    global g
    print(g)
    g=2
    print(g)

print(g)
change_print_global()
print_global()
print(globals())  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': ~~
print(__name__)  # __main__

