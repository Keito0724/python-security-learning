logs = [
    {"username": "alice", "success": True},
    {"username": "bob", "success": False},
    {"username": "bob", "success": False},
    {"username": "bob", "success": False},
    {"username": "admin", "success": False},
    {"username": "admin", "success": False},
    {"username": "charlie", "success": True}
]

class LogAnalyzer:
    def __init__(self,logs):
        self.logs = logs

    def count_success(self):
        count = 0
        for log in self.logs:
            if log["success"]:
                count += 1
        return count

    def count_failed(self):
        count = 0
        for log in self.logs:
            if not log["success"]:
                count += 1
        return count

    def count_user_failures(self):
        user_failures = {}
        for log in self.logs:
            if not log["success"]:
                name = log["username"]
                if name in user_failures:
                    user_failures[name] += 1
                else:
                    user_failures[name] = 1
        return user_failures

    def find_suspicious_users(self,threshold=3):
        user_failures = self.count_user_failures()
        suspicious_user = {}
        for name,count in user_failures.items():
            if count >= threshold:
                suspicious_user[name] = count
        return suspicious_user
        
analyzer = LogAnalyzer(logs)

print("Success:", analyzer.count_success())
print("Failed :", analyzer.count_failed())
print("Failure Count:", analyzer.count_user_failures())
print("Suspicious Users:", analyzer.find_suspicious_users(4))