import sys
import math

#Obtain input as string
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
print("Second Time Derivative of Mean Motion:           {0}".format(lines[1][44:53].strip()))
print("BSTAR Drag Term:                                 {0}".format(lines[1][53:62].strip()))
print("Ephemeris Type:                                  {0}".format(lines[1][62:64].strip()))
print("Element Set Number:                              {0}".format(lines[1][64:68].strip()))
print("Checksum:                                        {0}".format(lines[1][68:70].strip()))

print("\n")
print("Satellite Number:                                {0}".format(lines[2][2:8].strip()))
print("Inclination:                                     {0}".format(lines[2][8:17].strip()))
print("Right Ascension of Ascending Node:               {0}".format(lines[2][17:26].strip()))
print("Eccentricity:                                    {0}".format(lines[2][26:34].strip()))
print("Argument of Perigee:                             {0}".format(lines[2][34:43].strip()))
print("Mean Anomaly:                                    {0}".format(lines[2][43:52].strip()))
print("Mean Motion:                                     {0}".format(lines[2][52:63].strip()))
print("Revolutions at Epoch:                            {0}".format(lines[2][63:68].strip()))
print("Checksum:                                        {0}".format(lines[2][68:70].strip()))



