# WARN  - 9
# FATAL - 3
# INFO - 11493
# DEBUG - 6
# ERROR - 3

source_file = r"C:\Users\Arthur\Desktop\demo\sample_logs.log"
result_file = r"C:\Users\Arthur\Desktop\demo\found_logs.txt"
s_file = open(source_file)
r_file = open(result_file, 'w')

log_levels = ['INFO', 'DEBUG', 'WARN', 'ERROR', 'FATAL']
log_level_stats = {}


for line in s_file:
    for log_level in log_levels:
        if log_level in line:
            log_level_stats[log_level] = log_level_stats.get(log_level, 0) + 1
print(log_level_stats)


# for line in s_file:
#     if 'FATAL' in line:
#         r_file.write(line)
#
# s_file.close()
# r_file.close()




