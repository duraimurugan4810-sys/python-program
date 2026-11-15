


filename = "sample.log"


with open(filename, "w") as file:
    file.write("INFO: Application started\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: Application running\n")
    file.write("ERROR: Connection failed\n")


with open(filename, "r") as file:
    print("Log File Contents:\n")

    for line in file:
        print(line.strip())
