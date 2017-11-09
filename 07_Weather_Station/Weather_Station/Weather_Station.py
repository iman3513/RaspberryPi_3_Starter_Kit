import MCP3202
import os
from time import sleep

try:
	while True:
		os.system("clear")
		value1= MCP3202.readADC(0)
		voltage = round(float(value1 * 5000 / 4096), 2)
		temperature = (voltage - 550) / 10
		tampil = round(float(temperature), 2)
		print("Weather Station")
		print("Curent Temperature : ", tampil, u"\xb0", "C")
		print("")
		print("Press CTRL+C to exit")
		time.sleep(0.075)
		
except KeyboardInterrupt:
	print("exit")
