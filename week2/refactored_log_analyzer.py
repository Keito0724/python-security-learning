import json
import csv

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

csv_logs = load_csv("week2/login_logs.csv")
json_logs = load_json("week2/login_logs.json")

if csv_logs is not None:
    csv_report = create_report(csv_logs)
    print_report("CSV Report", csv_report)

if json_logs is not None:
    json_report = create_report(json_logs)
    print_report("JSON Report", json_report)

combined_report = {
    "csv": csv_report,
    "json": json_report
}

with open("week2/combined_report.json","w",encoding="utf-8") as file:
    json.dump(combined_report, file, indent=2,ensure_ascii=False)

