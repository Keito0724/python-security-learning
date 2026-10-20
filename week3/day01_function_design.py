logs = [
    {"username": "alice", "success": True},
    {"username": "bob", "success": False},
    {"username": "bob", "success": False},
    {"username": "bob", "success": False},
    {"username": "admin", "success": False},
    {"username": "admin", "success": False},
]


def count_success(logs: list) -> int:
    count = 0

    for log in logs:
        if log["success"]:
            count += 1

    return count


def count_failed(logs: list) -> int:
    count = 0

    for log in logs:
        if not log["success"]:
            count += 1

    return count


def count_user_failures(logs: list) -> dict:
    failure_count = {}

    for log in logs:
        if not log["success"]:
            username = log["username"]

            if username in failure_count:
                failure_count[username] += 1
            else:
                failure_count[username] = 1

    return failure_count


def find_suspicious_users(logs: list, threshold=3) -> dict:
    failure_count = count_user_failures(logs)
    suspicious_users = {}

    for username, count in failure_count.items():
        if count >= threshold:
            suspicious_users[username] = count

    return suspicious_users


def create_report(logs: list, threshold=3) -> dict:
    report = {
        "success": count_success(logs),
        "failed": count_failed(logs),
        "failure_count": count_user_failures(logs),
        "suspicious_users": find_suspicious_users(logs, threshold)
    }

    return report


report = create_report(logs, threshold=2)

print(report)