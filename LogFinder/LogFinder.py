original_log_file = open("/Users/amanasyan/Documents/Python projects/python-class/LogFinder/sample_logs.log", 'r')
found_logs = open("/Users/amanasyan/Documents/Python projects/python-class/LogFinder/results", 'w')

for line in original_log_file:
    if 'FATAL' in line:
        found_logs.write(line)


original_log_file.close()
found_logs.close()
