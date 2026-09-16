#Day3
username = input("ユーザー名: ")
password = input("パスワード: ")

passlen = len(password)

has_number = False
has_upper = False

for char in password:
    if char.isdigit():
        has_number = True

    if char.isupper():
        has_upper = True

    if has_number and has_upper:
        break

if passlen >= 12 and has_number and has_upper:
    print("Strong")
elif passlen >= 8 and has_number and has_upper:
    print("Medium")
else:
    print("Weak")