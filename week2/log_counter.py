def count_ip_access(filename):
    ip_dic = {}

    with open(filename, "r", encoding="utf-8") as file:
        for log in file:
            ip = log.strip()

            if ip in ip_dic:
                ip_dic[ip] += 1
            else:
                ip_dic[ip] = 1

    return ip_dic


filename = "week2/access.log"
ip_dic = count_ip_access(filename)

with open("week2/access_report.txt", "w", encoding="utf-8") as file:
    print("===== Access Report =====")
    file.write("===== Access Report =====\n")

    for ip, count in ip_dic.items():
        print(f"{ip} : {count}")
        file.write(f"{ip} : {count}\n")