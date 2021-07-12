import os
import sys


path = "C:/Users/Alexandre/AppData/Local/S2US/Screenshots/Runes/"
status = ["GOT", "SOLD"]

for s in status:
	count = 0
	check = True
	with os.scandir(path + s) as runes:
		print(s + " runes:")
		for rune in runes:
			check = True
			if not rune.is_file():
				continue
			for i in range(1, len(sys.argv)):
				if sys.argv[i].lower() not in rune.name.lower():
					check &= False
			if check:
				print(rune.name)
				count += 1
	print (count)
