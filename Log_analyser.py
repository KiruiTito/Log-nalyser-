def analyze_log(file_name):
    log_levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_name, "r") as f:
            for line in f:
                for level in log_levels:
                    if f"[{level}]" in line:
                        log_levels[level] += 1

        with open("report.txt", "w") as report:
            for level, count in log_levels.items():
                report.write(f"{level}: {count}\n")

        print("Log analysis complete. See report.txt")

    except FileNotFoundError:
        print("Log file not found.")
    except IOError as e:
        print("An I/O error occurred:", e)

# Run the analyzer
analyze_log("server.log")
