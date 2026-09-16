#1
for i in range(1,11):
    print(i)

#2
for i in range(1,11):
    if i % 2 == 0:
        print(i)
#3
users = ["alice", "bob", "admin", "guest"]
for char in users:
    print(f"User: {char}")

#4
password = "python123"
count = 0

for num in password:
    if num.isdigit():
        count = count+1

print(f"数字の数：{count}")

#5
ip_list = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.20",
    "172.16.0.1"
]

for ip in ip_list:
    if ip.startswith("192.168."):
        print(ip)

#6
num = int(input("数字を入力："))
total = 0

for i in range(1,num+1):
    total = total + i

print(f"合計：{total}")