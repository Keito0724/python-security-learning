import csv
import json 

def load_csv(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            logs = list(csv.DictReader(file))
    except FileNotFoundError:
        return None
    else:
        for log in logs:
            if log["success"] == "True":
                log["success"] = True
            else:
                log["success"] = False
        return logs


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
    failure_user = {}
    for log in logs:
        name = log["username"]
        if not log["success"]:
            if name in failure_user:
                failure_user[name] += 1
            else:
                failure_user[name] = 1
    return failure_user

def find_suspicious_users(logs):
    suspicious_user = {}
    failure_user = count_user_failures(logs)
    for name,count in failure_user.items():
        if count >= 3:
            suspicious_user[name] = count
    return suspicious_user

csv_logs = load_csv("week2/login_logs.csv")
json_logs = load_json("week2/login_logs.json")
report_csv = {}
report_json = {}

if csv_logs is not None:
    success = count_success(csv_logs)
    failed = count_failed(csv_logs)
    failed_dic = count_user_failures(csv_logs)
    failed_3times = find_suspicious_users(csv_logs)

    print("===== CSV Login Report =====")
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

    report_csv = {
        "success":success,
        "failed":failed,
    }

if json_logs is not None:
    success = count_success(json_logs)
    failed = count_failed(json_logs)
    failed_dic = count_user_failures(json_logs)
    failed_3times = find_suspicious_users(json_logs)

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

    report_json = {
        "success":success,
        "failed":failed,
    }

combined_report = {
    "csv" : report_csv,
    "json" : report_json
}
with open("week2/combined_report.json","w",encoding="utf-8") as file:
    json.dump(combined_report, file, indent=2,ensure_ascii=False)

