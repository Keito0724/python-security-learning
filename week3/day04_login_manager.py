class LoginMonitor:
    max_attempts = 3

    def __init__(self,username):
        self.username = username
        self.count_failed = 0

    def login_failed(self):
        self.count_failed += 1

    def login_success(self):
        self.count_failed = 0

    def is_suspicious(self) -> bool:
        return self.count_failed >= self.max_attempts

    def get_status(self) -> dict:
        dic_user = {
            "username": self.username,
            "failed_count": self.count_failed,
            "suspicious": self.is_suspicious()
        }

        return dic_user

    @classmethod
    def change_max_attempts(cls,new_value):
        cls.max_attempts = new_value

    @staticmethod
    def is_valid_username(username) -> bool:
        if isinstance(username,str):
            for char in username:
                if char.isspace():
                    return False
            if len(username) < 3:
                return False
            return True   
        else:
            return False

print(LoginMonitor.is_valid_username("alice"))
print(LoginMonitor.is_valid_username("ab"))
print(LoginMonitor.is_valid_username("alice bob"))
print(LoginMonitor.is_valid_username(123))

alice = LoginMonitor("alice")
bob = LoginMonitor("bob")

alice.login_failed()
alice.login_failed()

bob.login_failed()
bob.login_failed()

print(alice.get_status())
print(bob.get_status())

LoginMonitor.change_max_attempts(2)

print(alice.is_suspicious())
print(bob.is_suspicious())

alice.login_success()

print(alice.get_status())

        