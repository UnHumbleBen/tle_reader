import sys
import math

# Obtain input as string
raw_data = ''
tmp_line = ''
lines = []

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    else:
        raw_data += line

i = 0
for char in raw_data:
    if char != '\n':
        tmp_line += char
    else:
        lines.append(tmp_line)
        i += 1
        tmp_line = ''

print("{0}\n".format(lines))

epoch_time1 = float(lines[1][20:32].strip())
print("Epoch Day:                                       {0}".format(epoch_time1))

epoch_time2 = float(lines[4][20:32].strip())
print("Epoch Day:                                       {0}".format(epoch_time2))

time_diff = float(epoch_time2) - float(epoch_time1)
print("Time since epoch:                                {0}".format(time_diff))
DAY_TO_MINUTES = 1440
time_diff *= DAY_TO_MINUTES
print("Time since epoch (in minutes):                   {0}".format(time_diff))
