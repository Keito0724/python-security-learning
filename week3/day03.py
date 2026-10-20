#1
class Student:
    school = "University"

    def __init__(self,name):
        self.name = name

student1 = Student("alice")
student2 = Student("bob")

print(student1.name)
print(student1.school)
print(student2.name)
print(student2.school)

#2
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count

counter = Counter()

counter.increment()
counter.increment()
counter.increment()
counter.decrement()

print(counter.get_count())

#3 
class User:
    user_count = 0

    def __init__(self,name):
        self.name = name
        User.user_count += 1

user1 = User("alice")
user2 = User("bob")
user3 = User("charlie")

print(User.user_count)

#4
class LoginMonitor:
    max_attempts = 3

    def __init__(self, username):
        self.username = username
        self.count_failed = 0

    def login_failed(self):
        self.count_failed += 1

    def is_suspicious(self):
        return self.count_failed >= self.max_attempts

monitor = LoginMonitor("bob")

monitor.max_attempts = 5

monitor.login_failed()
monitor.login_failed()

print(monitor.is_suspicious())

monitor.login_failed()

print(monitor.is_suspicious())