# JSON Based Log File Analyzer

import json

logs = [
    {"message": "Application started", "level": "INFO"},
    {"message": "Login successful", "level": "INFO"},
    {"message": "File not found", "level": "ERROR"},
    {"message": "Invalid input", "level": "WARNING"},
    {"message": "Database error", "level": "ERROR"}
]

with open("logs.json", "w") as f:
    json.dump(logs, f, indent=4)

with open("logs.json", "r") as f:
    data = json.load(f)

info = 0
error = 0
warning = 0

for log in data:
    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "ERROR":
        error += 1
    elif log["level"] == "WARNING":
        warning += 1

print("----- LOG ANALYSIS -----")
print("INFO messages:", info)
print("ERROR messages:", error)
print("WARNING messages:", warning)
print("Total logs:", len(data))