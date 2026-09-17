login_logs = [
    {"username": "alice", "success": True},
    {"username": "bob", "success": False},
    {"username": "admin", "success": False},
    {"username": "bob", "success": False},
    {"username": "charlie", "success": True},
    {"username": "admin", "success": False}
]

success_count = 0
failed_count = 0
admin_failed = 0

for log in login_logs:
    if log["success"] == True:
        success_count += 1
    else:
        failed_count += 1
        if log["username"] == "admin":
            admin_failed += 1

print("===== Login Report =====")
print(f"Success:    {success_count}")
print(f"Failed:     {failed_count}")
print(f"admin failed:   {admin_failed}")

    