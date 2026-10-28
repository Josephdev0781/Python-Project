# 1. Standard library functions/ buildin/ pre define-- functions that already exist

x = min(6, 4, 5, 7, 9, 1, 6)
print("min = ", x)
y = max(6, 4, 5, 7, 9, 1, 6)
print("max = ", y)

# 2. user defined functions

def school():
    print("emobilis")

school()

def add():
    x = 10
    y = 20
    print(x + y)
add()

def avg():
    x = min(6, 4, 5, 7, 9, 1, 6)
    y = max(6, 4, 5, 7, 9, 1, 6)
    print(int((x + y) / 2))
avg()


#parameter variable
def add(x, y):
    print(x + y)

add(5, 6)
add(8, 6)
add(3, 7)
#argument is the value passed( 5 and 6 are arguments)

