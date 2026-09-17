#1
users = ["alice", "bob", "charlie", "admin"]

for user in users:
    print(user)
    if user == "admin":
        print("管理者を発見")

#2
number = []

number.append(1)
number.append(2)
number.append(3)
number.append(4)
number.append(5)

print(number)

#3
user = {
    "name": "alice",
    "role": "admin",
    "login_count": 3
}

print(f"Name:{user['name']}")
print(f"Role:{user['role']}")

#4
user["login_count"] = user["login_count"] + 1

#5
logs = [
    {"ip": "192.168.1.10", "status": 200},
    {"ip": "10.0.0.5", "status": 404},
    {"ip": "192.168.1.20", "status": 403},
    {"ip": "172.16.0.1", "status": 200}
]

for log in logs:
    if log["status"] >= 400:
        print(f"{log['ip']}:{log['status']}")

#6
ip_list = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.10",
    "172.16.0.1",
    "192.168.1.10"
]

count = 0

for ip in ip_list:
    if ip == "192.168.1.10":
        count = count + 1

print(f"回数:{count}")