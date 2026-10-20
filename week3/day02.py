#1
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Student("Allice",20)
print(student1.name)
print(student1.age)

#2
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

student1 = Student("Allice",20)
print(student1.name)
print(student1.age)
student1.introduce()

#3
student1 = Student("alice", 20)
student2 = Student("bob", 21)
student1.introduce()
student2.introduce()

#4
class LoginLog:
    def __init__(self,username,success):
        self.username = username
        self.success = success

    def is_success(self):
        return self.success


log1 = LoginLog("alice", True)
log2 = LoginLog("bob", False)

print(log1.is_success())
print(log2.is_success())