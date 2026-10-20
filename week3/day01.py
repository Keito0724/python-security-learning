#1
def multiply(a,b):
    return a * b

print(multiply(3, 4))

#2
def greet(name, message="Hello"):
    print(f"{message},{name}")

greet("Alice", "Good morning")

#3
def count_user_failures(logs):
    None

def find_suspicious_users(logs, threshold=3):
    suspicious_user = {}
    failure_user = count_user_failures(logs)
    for name,count in failure_user.items():
        if count >= threshold:
            suspicious_user[name] = count
    return suspicious_user

#4
def count_failed(logs:list[dict]) -> int:
    count = 0

    for log in logs:
        if not log["success"]:
            count += 1

    return count

#5