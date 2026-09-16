#1
number = int(input("整数："))

if number > 0:
    print("正の数")
elif number == 0:
    print("0")
else:
    print("負の数")

#2

#3
x = number % 2
if x == 0:
    print("偶数")
else:
    print("奇数")

#4

#5
username = input("ユーザー名")
password = input("パスワード")

if username == "admin" and password == "security123":
    print("ログイン成功")
else:
    print("ログイン失敗")

#6
x = int(input("数字:"))
y = int(input("数字:"))
z = int(input("数字:"))

maxnum = x

if maxnum < y:
    maxnum = y
if maxnum < z:
    maxnum = z

print(f"最大値:{maxnum}")