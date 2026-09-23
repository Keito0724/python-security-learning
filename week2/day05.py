import csv
import json

#1
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

filename = "week2/login_logs.csv"
logs = load_csv(filename)
if logs is not None:
    for log in logs:
        print(log)

#2
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

#3
def count_success(logs):
    count = 0
    for log in logs:
        if log["success"]:
            count += 1
    return count

#4
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
