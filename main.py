# Main controller

from log_parser import read_logs
from alert_generator import detect_bruteforce, detect_sql, detect_xss

logs = read_logs("logs/sample_log.txt")

bruteforce_count = detect_bruteforce(logs)
sql_count = detect_sql(logs)
xss_count = detect_xss(logs)

print("====== ALERT SUMMARY ====")

print("Failed Logins:", bruteforce_count)
print("SQL Injection Attempts:", sql_count)
print("XSS Attempts:", xss_count)

