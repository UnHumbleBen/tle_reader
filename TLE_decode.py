import sys
import math

# Useful Conversions
REVOLUTIONS_TO_RADIANS = 2 * math.pi
DAYS_TO_MINUTES = 1440

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

print("Name:                                            {0}".format(lines[0].strip()))
print("Number:                                          {0}".format(lines[1][2:7].strip()))
print("Classification:                                  {0}".format(lines[1][7].strip()))
print("Launch Year:                                     {0}".format(lines[1][8:11].strip()))
print("Launch Number:                                   {0}".format(lines[1][11:14].strip()))
print("Piece:                                           {0}".format(lines[1][14:18].strip()))
print("Epoch Year:                                      {0}".format(lines[1][18:20].strip()))

epoch_time = float(lines[1][20:32].strip())
epoch_day = math.floor(epoch_time) 
print("Epoch Day:                                       {0}".format(epoch_day))
epoch_time = epoch_time - epoch_day 
epoch_hour = 24 * epoch_time
print("Epoch Hour:                                      {0}".format(epoch_hour))
epoch_hour = epoch_hour - math.floor(epoch_hour)
epoch_minute = 60 * epoch_hour
print("Epoch Minute:                                    {0}".format(epoch_minute))
epoch_minute = epoch_minute -  math.floor(epoch_minute)
epoch_second = 60 * epoch_minute
print("Epoch Second:                                    {0}".format(epoch_second))

print("First Time Derivative of Mean Motion:            {0}".format(lines[1][32:44].strip()))
n0_dot = lines[1][32:44].strip()
n0_dot = float(n0_dot) # rev per day squared
print("----n0_dot", n0_dot, "rev per day squared")
n0_dot = n0_dot * REVOLUTIONS_TO_RADIANS / (DAYS_TO_MINUTES * DAYS_TO_MINUTES) # radians per min squared

print("----n0_dot", n0_dot, "radians per min squared")

print("Second Time Derivative of Mean Motion:           {0}".format(lines[1][44:53].strip()))
temp = lines[1][44:53]
mantissa = temp[0:6]
power = temp[-3:]
mantissa = int(mantissa)
power = int(power)
n0_double_dot = (mantissa / 100000) ** power
print("----n0_double_dot", n0_double_dot)

print("BSTAR Drag Term:                                 {0}".format(lines[1][53:62].strip()))
print("Ephemeris Type:                                  {0}".format(lines[1][62:64].strip()))
print("Element Set Number:                              {0}".format(lines[1][64:68].strip()))
print("Checksum:                                        {0}".format(lines[1][68:70].strip()))

print("\n")
print("Satellite Number:                                {0}".format(lines[2][2:8].strip()))
print("Inclination:                                     {0}".format(lines[2][8:17].strip()))
i0 = lines[2][8:17].strip()
i0 = float(i0)
print("----i0", i0)

print("Right Ascension of Ascending Node:               {0}".format(lines[2][17:26].strip()))
omega0 = lines[2][17:26].strip()
omega0 = float(omega0)
print("----omega0", omega0)

print("Eccentricity:                                    {0}".format(lines[2][26:34].strip()))
e0 = lines[2][26:34].strip()
e0 = float(e0) / (10 ** 7)
print("----e0", e0)

print("Argument of Perigee:                             {0}".format(lines[2][34:43].strip()))
w0 = lines[2][34:43].strip()
w0 = float(w0) 
print("----w0", w0)

print("Mean Anomaly:                                    {0}".format(lines[2][43:52].strip()))
M0 = lines[2][43:52].strip()
M0 = float(M0)
print("----M0", M0)

print("Mean Motion:                                     {0}".format(lines[2][52:63].strip()))
n0 = lines[2][52:63].strip()
n0 = float(n0)
print("----n0", n0)

print("Revolutions at Epoch:                            {0}".format(lines[2][63:68].strip()))
print("Checksum:                                        {0}".format(lines[2][68:70].strip()))

// Initializing constants
k_e = 0.0743669161
a1 = (k_e / n0) ** (2 / 3) 
