#1
report = {
    "success": 2,
    "failed": 5,
    "failure_count": {
        "bob": 3,
        "admin": 2
    }
}

print(f"Success: {report["success"]}")
print(f"Failed: {report['failed']}")

#2
for name, count in report["failure_count"].items():
    print(f"{name}: {count}")

#3
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

#4
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

