username = input("ユーザー名")
password = input("パスワード")

passlen = len(password)

if passlen < 8:
    print("Weak")
elif passlen < 12:
    print("Medium")
else:
    print("Strong")