def read_logs(file_path):
    with open(file_path, "r")as file:
        for line in file:
            yield line.strip()
logs = read_logs("logs.txt")

for log in logs:
    if "ERROR" in log:
        print(log)
