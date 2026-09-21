import json

def load_logs(filename):
    with open(filename,"r",encoding="utf-8") as file:
        logs = json.load(file)
    return logs

def count_success(logs):
    count = 0
    for log in logs:
        if log["success"]:
            count += 1

    return count

def count_failed(logs):
    count = 0
    for log in logs:
        if not log["success"]:
            count += 1
    return count

def count_user_failures(logs):
    failed_dic = {}
    for log in logs:
        if not log["success"]:
            name = log["username"]
            if name in failed_dic:
                failed_dic[name] += 1
            else:
                failed_dic[name] = 1
    return failed_dic

def find_suspicious_users(logs):
    failed_3times = {}
    failed_dic = count_user_failures(logs)
    for name,count in failed_dic.items():
        if count >= 3:
            failed_3times[name] = count
    return failed_3times

filename = "week2/login_logs.json"
logs = load_logs(filename)
success = count_success(logs)
failed = count_failed(logs)
failed_dic = count_user_failures(logs)
failed_3times = find_suspicious_users(logs)

print("===== JSON Login Report =====")
print()
print(f"Success: {success}")
print(f"Failed : {failed}")
print()
print("Failure Count")
for name,count in failed_dic.items():
    print(f"{name}: {count}")
print()
print("Suspicious User")
for name,count in failed_3times.items():
    print(f"{name}: {count} failed attempts")

report = {
    "success":success,
    "failed":failed,
    "failure_count":failed_dic,
    "suspicious_users":failed_3times
}

with open("week2/json_report.json","w",encoding="utf-8") as file:
    json.dump(report, file, indent=4,ensure_ascii=False)
    