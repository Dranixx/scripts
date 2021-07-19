import argparse
import os
import re


path = "C:/Users/Alexandre/AppData/Local/S2US/Screenshots/Runes/"
status = ["GOT", "SOLD"]

def main():
	parser = argparse.ArgumentParser(description='TODO...')

	parser.add_argument('query', type=str, help="regex query")
	parser.add_argument('-v', '--verbose', action='store_true', help="print every rune name")

	args = parser.parse_args()

	for s in status:
		count = 0
		with os.scandir(path + s) as runes:
			print(s + " runes:")
			for rune in runes:
				if not rune.is_file():
					continue
				if re.search(args.query, rune.name):
					if args.verbose:
						print(rune.name)
					count += 1
		print (count)



if __name__ == "__main__":
	main()