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

def load_txt(filename):
    try:
        with open(filename,"r",encoding="utf-8") as file:
            text = file.readlines()
    except FileNotFoundError:
        return None
    else:
        logs = []
        for log in text:
            parts = log.strip().split(",")
            ip = parts[0]
            username = parts[1]
            success = parts[2] == "True"
            data = {
                "ip" : ip,
                "username" : username,
                "success" : success
            }
            logs.append(data)
        return logs

def load_logs(filename):
    if filename.endswith(".csv"):
        return load_csv(filename)
    elif filename.endswith(".json"):
        return load_json(filename)
    elif filename.endswith(".txt"):
        return load_txt(filename)
    else:
        print("Error: Unsupported file format")
        return None
    
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

def create_report(logs):
    report = {
        "success" : count_success(logs),
        "failed" : count_failed(logs),
        "failure_count" : count_user_failures(logs),
        "suspicious_users" : find_suspicious_users(logs)
    }
    return report

def print_report(title, report):
    print(f"===== {title} =====")
    print()
    print(f"Success: {report["success"]}")
    print(f"Failed : {report["failed"]}")
    print()
    print("Failure Count")
    for name,count in report["failure_count"].items():
        print(f"{name}: {count}")
    print()
    print("Suspicious Users")
    for name,count in report["suspicious_users"].items():
        print(f"{name}: {count} failed attempts")

def save_report(filename, report):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            json.dump(report,file,indent = 4,ensure_ascii=False)
    except OSError:
        print("Error: Can't Write")


filename = "week2/login_logs.csv"

logs = load_logs(filename)

if logs is not None:
    report = create_report(logs)
    print_report(filename, report)
    save_report("week2/final_report.json", report)