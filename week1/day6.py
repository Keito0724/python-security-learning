#1
login_logs = [
    {"username": "alice", "success": True},
    {"username": "bob", "success": False},
    {"username": "admin", "success": False},
    {"username": "bob", "success": False},
    {"username": "charlie", "success": True},
    {"username": "admin", "success": False}
]

def count_failed(logs):
    count = 0
    for log in logs:
        if log["success"] == False:
            count += 1
    return count 

failed = count_failed(login_logs)
print(failed)

#2
def count_admin_failed(logs):
    count = 0
    for log in logs:
        if log["username"] == "admin" and log["success"] == False:
            count += 1
    return count

#3
login_logs = [
    {"username": "alice", "success": True},
    {"username": "bob", "success": False},
    {"username": "admin", "success": False},
    {"username": "bob", "success": False},
    {"username": "charlie", "success": True},
    {"username": "admin", "success": False},
    {"username": "bob", "success": False}
]

def count_3times_failed(logs):
    failed_counts = {}

    for log in logs:
        if log["success"] == False:
            failed_name = log["username"]
            if failed_name in failed_counts:
                failed_counts[failed_name] += 1
            else:
                failed_counts[failed_name] = 1

    return failed_counts

countfailed = count_3times_failed(login_logs)
for i in countfailed:
    if countfailed[i] >= 3:
        print(f"Suspicious user: {i}")

#4
logs = [
    {"ip": "192.168.1.10", "status": 200},
    {"ip": "10.0.0.5", "status": 404},
    {"ip": "192.168.1.20", "status": 403},
    {"ip": "172.16.0.1", "status": 200},
    {"ip": "10.0.0.5", "status": 404}
]

def count_errors(logs):
    count_error = 0
    for log in logs:
        if log["status"] >= 400:
            count_error += 1

    return count_error

error = count_errors(logs)
print(error)

#5
logs = [
    {"ip": "192.168.1.10", "status": 200},
    {"ip": "10.0.0.5", "status": 404},
    {"ip": "192.168.1.20", "status": 403},
    {"ip": "172.16.0.1", "status": 200},
    {"ip": "10.0.0.5", "status": 404}
]

def acess_ip(logs):
    dic_acess = {}
    for log in logs:
        acess_user = log["ip"]
        if log["ip"] in dic_acess:
            dic_acess[acess_user] += 1
        else:
            dic_acess[acess_user] = 1
    return dic_acess

counts = acess_ip(logs)

print(counts)