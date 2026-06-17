# Read the sample_log.txt and returns all lines

def read_logs(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()
    return logs
    # Opens the log file in read mode and reads all lines into a list called logs, which is then returned