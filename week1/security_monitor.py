logs = [
    {"ip": "192.168.1.10", "username": "alice", "success": True},
    {"ip": "10.0.0.5", "username": "bob", "success": False},
    {"ip": "10.0.0.5", "username": "bob", "success": False},
    {"ip": "192.168.1.20", "username": "admin", "success": False},
    {"ip": "172.16.0.1", "username": "charlie", "success": True},
    {"ip": "10.0.0.5", "username": "bob", "success": False},
    {"ip": "192.168.1.20", "username": "admin", "success": False},
    {"ip": "10.0.0.8", "username": "admin", "success": False},
    {"ip": "10.0.0.8", "username": "admin", "success": False},
    {"ip": "10.0.0.8", "username": "admin", "success": False}
]

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

def count_ip_access(logs):
    count_ip = {}
    for log in logs:
        log_ip = log["ip"]
        if log_ip in count_ip:
            count_ip[log_ip] += 1
        else:
            count_ip[log_ip] = 1
    return count_ip

def count_user_failures(logs):
    count_failed_user = {}
    for log in logs:
        log_name = log["username"]
        if not log["success"]:
            if log_name in count_failed_user:
                count_failed_user[log_name] += 1
            else:
                count_failed_user[log_name] = 1
    return count_failed_user

def count_ip_failures(logs):
    count_failed_ip = {}
    for log in logs:
        log_ip = log["ip"]
        if not log["success"]:
            if log_ip in count_failed_ip:
                count_failed_ip[log_ip] += 1
            else:
                count_failed_ip[log_ip] = 1
    return count_failed_ip

def find_suspicious_ips(logs):
    failed_3times = {}
    count_failed_ip = count_ip_failures(logs)
    for ip,count in count_failed_ip.items():
        if count >= 3:
            failed_3times[ip] = count
    return failed_3times

def count_admin_failures(logs):
    count_attck = 0
    count_failed_user = count_user_failures(logs)
    for name,count in count_failed_user.items():
        if name == "admin":
            count_attck = count
    return count_attck

def security_level(logs):
    failed_3times = find_suspicious_ips(logs)
    count = len(failed_3times)
    if count == 0:
        return "LOW"
    elif count == 1:
        return "MEDIUM"
    else:
        return "HIGH"

success = count_success(logs)
failed = count_failed(logs)
access_ip = count_ip_access(logs)
failed_user = count_user_failures(logs)
failed3times_ip = find_suspicious_ips(logs)
attck_admin = count_admin_failures(logs)
level = security_level(logs)

print("===== Security Monitor =====")

print("\nLogin Summary")
print(f"Success: {success}")
print(f"Failed: {failed}")

print("\nIP Access Count")
for ip,count in access_ip.items():
    print(f"{ip}:{count}")

print("\nUser Failure Count")
for name,count in failed_user.items():
    print(f"{name}:{count}")

print("\nSuspicious IP")
for ip,count in failed3times_ip.items():
    print(f"{ip}:{count} failed attempts")

print(f"\nAdmin Failed Attempts : {attck_admin}")

print(f"\nSecurity Level : {level}")