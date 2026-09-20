import csv

#1
with open("week2/login_logs.csv","r",encoding="utf-8") as file:
    logs = csv.reader(file)

    for log in logs:
        print(log)

#2
with open("week2/login_logs.csv", "r", encoding="utf-8") as file:
    logs = csv.DictReader(file)

    for log in logs:
        print(f"User: {log['username']}")

#3
with open("week2/login_logs.csv", "r", encoding="utf-8") as file:
    logs = csv.DictReader(file)

    for log in logs:
        if log["success"] == "False":
            print(f"Failed: {log['username']}")

#4
with open("week2/login_logs.csv","r",encoding="utf-8") as file:
    logs = csv.DictReader(file)
    ip_dic = {}

    for log in logs:
        ip = log["ip"]
        if ip in ip_dic:
            ip_dic[ip] += 1
        else:
            ip_dic[ip] = 1

print(ip_dic)

#5
with open("week2/login_logs.csv", "r", encoding="utf-8") as file:
    logs = csv.DictReader(file)
    failed_dic = {}

    for log in logs:
        if log["success"] == "False":
            user = log["username"]

            if user in failed_dic:
                failed_dic[user] += 1
            else:
                failed_dic[user] = 1

print(failed_dic)