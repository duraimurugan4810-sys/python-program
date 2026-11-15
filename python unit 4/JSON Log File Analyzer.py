
import json

filename = "logs.json"


logs = [
    {"level": "INFO", "message": "Application started"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "ERROR", "message": "Connection failed"},
    {"level": "INFO", "message": "Application running"}
]


with open(filename, "w") as file:
    json.dump(logs, file, indent=4)


with open(filename, "r") as file:
    data = json.load(file)


info_count = 0
warning_count = 0
error_count = 0

print("JSON Log File Analyzer")
print("----------------------")

for log in data:
    print(log["level"], ":", log["message"])

    if log["level"] == "INFO":
        info_count += 1
    elif log["level"] == "WARNING":
        warning_count += 1
    elif log["level"] == "ERROR":
        error_count += 1


print("\nLog Analysis Summary")
print("INFO Count:", info_count)
print("WARNING Count:", warning_count)
print("ERROR Count:", error_count)
print("Total Logs:", len(data))
