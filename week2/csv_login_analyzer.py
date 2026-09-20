import csv

def count_success(filename):
    count = 0

    with open(filename,"r",encoding="utf-8") as file:
        logs = csv.DictReader(file)

        for log in logs:
            if log["success"] == "True":
                count += 1

    return count


def count_failed(filename):
    count = 0
        
    with open(filename,"r",encoding="utf-8") as file:
        logs = csv.DictReader(file)
    
        for log in logs:
            if log["success"] == "False":
                count += 1
    
    return count

    
def count_user_failures(filename):
    failed_dic = {}
    with open(filename,"r",encoding="utf-8") as file:
        logs = csv.DictReader(file)

        for log in logs:
            if log["success"] == "False":
                user = log["username"]
                if user in failed_dic:
                    failed_dic[user] += 1
                else:
                    failed_dic[user] = 1

    return failed_dic
    
def find_suspicious_users(filename):
    failed_dic = count_user_failures(filename)
    failed3_dic = {}

    for name,count in failed_dic.items():
        if count >= 3:
            failed3_dic[name] = count

    return failed3_dic

filename = "week2/login_logs.csv"
success = count_success(filename)
failed = count_failed(filename)
failed_dic = count_user_failures(filename)
failed3_dic = find_suspicious_users(filename)

print("===== CSV Login Report =====\n\n")
print(f"Success :   {success}")
print(f"Failed  :   {failed}")

print(f"\nFailed Count")
for name,count in failed_dic.items():
    print(f"{name}  :   {count}")

print(f"\nSuspicious User")
for name,count in failed3_dic.items():
    print(f"{name}  :   {count} failed attempts")
    