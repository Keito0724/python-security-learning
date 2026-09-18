logs = [
    {"ip": "192.168.1.10", "username": "alice", "success": True},
    {"ip": "10.0.0.5", "username": "bob", "success": False},
    {"ip": "10.0.0.5", "username": "bob", "success": False},
    {"ip": "192.168.1.20", "username": "admin", "success": False},
    {"ip": "172.16.0.1", "username": "charlie", "success": True},
    {"ip": "10.0.0.5", "username": "bob", "success": False},
    {"ip": "192.168.1.20", "username": "admin", "success": False}
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
    access_ip = {}
    for log in logs:
        ip_name = log["ip"]
        if ip_name in access_ip:
            access_ip[ip_name] += 1
        else:
            access_ip[ip_name] = 1
    return access_ip

def find_suspicious_ips(logs):
    access_ip = {}
    for log in logs:
        ip_name = log["ip"]
        if not log["success"]:
           if ip_name in access_ip:
            access_ip[ip_name] += 1
           else:
            access_ip[ip_name] = 1 

    failed3time_ip = {}
    for ip,count in access_ip.items():
        if count >= 3:
            failed3time_ip[ip] = count
    return failed3time_ip 

success = count_success(logs)
failed = count_failed(logs)
access_ip = count_ip_access(logs)
failed3times = find_suspicious_ips(logs)

print("===== Security Log Report =====")
print(f"Success:    {success}")
print(f"Failed:     {failed}")
print("\nIP Access Count")
for ip, count in access_ip.items():
    print(f"{ip}: {count}")

print("\nSuspicious IP")
for ip, count in failed3times.items():
    print(f"{ip}: {count} failed attempts")
