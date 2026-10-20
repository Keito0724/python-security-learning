#1
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}. I am {self.age} years old.")

user1 = User("alice", 20)

user1.introduce()

#2
class LoginMonitor:
    max_attempts = 3

    @classmethod
    def change_max_attempts(cls,new_value):
        cls.max_attempts = new_value

print(LoginMonitor.max_attempts)

LoginMonitor.change_max_attempts(5)

print(LoginMonitor.max_attempts)

#3
class SecurityUtils:

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8

print(SecurityUtils.is_valid_password("abc123"))
print(SecurityUtils.is_valid_password("password123"))

#4
class LoginMonitor:
    max_attempts = 3

    def __init__(self, username):
        self.username = username
        self.failed_count = 0

    def login_failed(self):
        self.failed_count += 1

    def is_suspicious(self) -> bool:
        return self.failed_count >= self.max_attempts

    @classmethod
    def change_max_attempts(cls, new_value):
        cls.max_attempts = new_value

    @staticmethod
    def is_admin(username) -> bool:
        return username == "admin"

bob = LoginMonitor("bob")

bob.login_failed()
bob.login_failed()

print(bob.is_suspicious())

LoginMonitor.change_max_attempts(2)

print(bob.is_suspicious())
print(LoginMonitor.is_admin("admin"))