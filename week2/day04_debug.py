#1
try:
    number = int(input("Number: "))
    print(f"Number: {number}")
except ValueError:        
    print("数字を入力")

#2
try:
    with open("week2/sample.txt","r",encoding="utf-8") as file:
        text = file.read()
    print(text)
except FileNotFoundError:
    print("ファイルが存在しません")

#3
import json
try:
    with open("week2/login_logs.json","r",encoding="utf-8") as file:
        logs = json.load(file)
except FileNotFoundError:
    print("ファイルが存在しません")
except json.JSONDecodeError:
    print("ファイル形式が崩れています")
else:
    print(logs)

#4
def load_json(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            logs = json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    else:
        return logs

filename = "week2/login_logs.json"
logs = load_json(filename)

if logs is not None:
    for log in logs:
        print(log["username"])