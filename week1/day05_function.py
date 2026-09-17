#1
def hello():
    print("Hello Python")

hello()

#2
def greet(name):
    print(f"Hello,{name}")

greet(input("名前："))

#3
def add(x,y):
    return x+y

result = add(2,3)
print(result)

#4
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(2))

#5
def has_number(char):
    for i in char:
        if i.isdigit():
            return True

    return False

#6
numbers = [10, 25, 8, 40, 3]

def find_max(number):
    maxnum = number[0]
    for i in number:
        if maxnum < i:
            maxnum = i

    return maxnum