# Log File Reader

file = "sample.log"

# Create a sample log file
with open(file, "w") as f:
    f.write("Application started\n")
    f.write("User logged in\n")
    f.write("Error occurred\n")
    f.write("Application closed\n")

# Read the log file
with open(file, "r") as f:
    print("----- LOG FILE CONTENTS -----")
    for line in f:
        print(line.strip())