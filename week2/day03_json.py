import json
#1
with open("week2/login_logs.json","r",encoding="utf-8") as file:
    text = json.load(file)

print(text)
print(type(text))
print(type(text[0]))

#2
with open("week2/login_logs.json","r",encoding="utf-8") as file:
    logs = json.load(file)

for log in logs:
    print(f"User: {log["username"]}")

#3
for log in logs:
    if not log["success"]:
        print(f"Failed: {log["username"]}")

#4
ip_count = {}
for log in logs:
    ip = log["ip"]
    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

print(ip_count)

#5
failed_count = {}
for log in logs:
    name = log["username"]
    if not log["success"]:
        if name in failed_count:
            failed_count[name] += 1
        else:
            failed_count[name] = 1

print(failed_count)
