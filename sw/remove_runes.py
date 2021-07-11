import os


path = "C:/Users/Alexandre/AppData/Local/S2US/Screenshots/Runes/SOLD/"
count = 0
useless = {"[ATK]", "[HP]", "[DEF]"}

with os.scandir(path) as runes:
	for rune in runes:
		if not rune.is_file():
			continue
		lr = rune.name.split(" ")
		if int(lr[5][2]) % 2 == 0:
			if lr[6] in useless:
				print(rune.name)
				count += 1
				os.remove(path + rune.name)
	print("Deleted " + str(count)+ " runes" )


