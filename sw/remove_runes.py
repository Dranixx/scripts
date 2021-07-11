import os


path = "C:/Users/Alexandre/AppData/Local/S2US/Screenshots/Runes/SOLD/"
count = 0

with os.scandir(path) as runes:
	for rune in runes:
		if rune.name



print(len(runes))