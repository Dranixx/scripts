from collections import defaultdict
import argparse
import os
import re

path = "C:/Users/Alexandre/AppData/Local/S2US/Screenshots/Runes/"
status = ["GOT", "SOLD"]
types = defaultdict(int)
total = 0

def main():
	parser = argparse.ArgumentParser(description='This program show some stats about my dropped runes.')

	parser.add_argument('query', type=str, help="regex query")
	parser.add_argument('-v', '--verbose', action='store_true', help="print every rune name")
	parser.add_argument('-t', '--type', action='store_true', help="count rune type")

	args = parser.parse_args()

	total = 0

	for s in status:
		count = 0
		with os.scandir(path + s) as runes:
			print(s + " runes:")
			for rune in runes:
				if not rune.is_file():
					continue
				if re.search(args.query, rune.name, re.IGNORECASE):
					if args.verbose:
						print(rune.name)
					if args.type:
						lr = rune.name.split(" ")
						types[lr[1]] += 1
					count += 1
		if args.type:
			print("Types: " + str(dict(types)))
		print("Count: " + str(count))
		total += count
		print("======================================================")
	print("Total: " + str(total))


if __name__ == "__main__":
	main()
