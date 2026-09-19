#1
with open("week2/sample.txt","r") as file:
    text = file.read()
print(text)

#2
with open("week2/sample.txt","r") as file:
    text = file.readlines()
for line in text:
    name = line.strip()
    print(f"User: {name}")

#3
for line in text:
    name = line.strip()
    if name == "admin":
        print("Admin Detected")

#4
with open("week2/access.log","r") as file:
    logs = file.readlines()

log_dic = {}
for log in logs:
    ip = log.strip()
    if ip == "192.168.1.10":
        if ip in log_dic:
            log_dic[ip] += 1
        else:
            log_dic[ip] = 1
print(log_dic)

#5
all_log_dic ={}
for log in logs:
    ip = log.strip()
    if ip in all_log_dic:
        all_log_dic[ip] += 1
    else:
        all_log_dic[ip] = 1
print(all_log_dic)