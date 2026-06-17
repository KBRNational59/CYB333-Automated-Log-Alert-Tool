# Identify suspicious activity provided by logs

def detect_bruteforce(logs):
    failed_count = 0

    for line in logs:
        if "LOGIN FAILED" in line:
            failed_count += 1

    return failed_count


def detect_sql(logs):
    sql_count = 0

    for line in logs:
        if "SELECT" in line:
            sql_count += 1

    return sql_count


def detect_xss(logs):
    xss_count = 0

    for line in logs:
        if "<script>" in line:
            xss_count += 1

    return xss_count