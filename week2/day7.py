#1
line = "10.0.0.5,bob,False"
parts = line.strip().split(",")

ip = parts[0]
username = parts[1]
success = parts[2] == "True"

print(ip)
print(username)
print(success)

#2
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

def load_csv(filename):
    None

def load_json(filename):
    None

#3
def load_logs(filename):
    if filename.endswith(".csv"):
        return load_csv(filename)
    elif filename.endswith(".json"):
        return load_json(filename)
    elif filename.endswith("txt"):
        return load_txt(filename)
    else:
        print("Error: Unsupported file format")
        return None
