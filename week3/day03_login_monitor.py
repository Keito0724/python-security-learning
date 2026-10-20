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

alice = LoginMonitor("alice")
bob = LoginMonitor("bob")
alice.max_attempts = 5
bob.max_attempts = 2

alice.login_failed()
alice.login_failed()
alice.login_success()

bob.login_failed()
bob.login_failed()
bob.login_failed()

print(alice.get_status())
print(bob.get_status())
