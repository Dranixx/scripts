from collections import defaultdict
import argparse
import os
import pprint
import re

path = "C:/Users/Alexandre/AppData/Local/S2US/Screenshots/Runes/"
status = ["GOT", "SOLD"]
cost_dict = {"[+0]": 0,"[+3]": 4425, "[+6]": 21710, "[+9]": 77847, "[+12]": 248080}

def main():
	parser = argparse.ArgumentParser(description='This program show some stats about my dropped runes.')

	parser.add_argument('query', type=str, help="regex query")
	parser.add_argument('-v', '--verbose', action='store_true', help="print every rune name")
	parser.add_argument('-t', '--type', action='store_true', help="count rune type")
	parser.add_argument('-c', '--cost', action='store_true', help="Cost power up runes ")

	args = parser.parse_args()

	total = 0
	costs = 0

	for s in status:
		cost = 0
		count = 0
		types = defaultdict(int)
		with os.scandir(path + s) as runes:
			print(s + " runes:")
			for rune in runes:
				if not rune.is_file():
					continue
				if re.search(args.query, rune.name, re.IGNORECASE):
					lr = rune.name.split(" ")
					if args.verbose:
						print(rune.name)
					if args.type:
						types[lr[1]] += 1
					if args.cost:
						cost += cost_dict[lr[3]]
					count += 1
		if args.type:
			print("Types: ", end="")
			pprint.pprint(dict(types))
		print("Count: " + str(count))
		if args.cost:
			print("Cost: " + f'{cost:,}')
			costs += cost
		total += count
		print("======================================================")
	print("Total: " + str(total))
	print("Total Cost: " + f'{costs:,}')


if __name__ == "__main__":
	main()
