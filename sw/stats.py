from collections import defaultdict
import argparse
import os
import pprint
import re

path = f"C:/Users/{os.getlogin()}/AppData/Local/S2US/Screenshots/Runes/"
status = ["GOT", "SOLD"]
cost_dict = {"[+0]": 0,"[+3]": 4425, "[+6]": 21710, "[+9]": 77847, "[+12]": 248080}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
	parser = argparse.ArgumentParser(description='This program show some stats about my dropped runes.')

	parser.add_argument('query', type=str, help="regex query")
	parser.add_argument('-v', '--verbose', action='store_true', help="print every rune name")

	args = parser.parse_args()

	total = 0
	costs = 0
	sumtypes = dict()
	allslots = defaultdict(int)

	print("===========================================================================================================")
	for s in status:
		cost = 0
		count = 0
		types = defaultdict(int)
		slots = defaultdict(int)
		color = bcolors.OKGREEN if s == "GOT" else bcolors.FAIL
		with os.scandir(path + s) as runes:
			print(bcolors.BOLD +  s + " runes:" + bcolors.ENDC)
			for rune in runes:
				# Skip directory
				if not rune.is_file():
					continue
				# Begin search
				if re.search(args.query, rune.name, re.IGNORECASE):
					lr = rune.name.split(" ")
					if args.verbose:
						print(color + rune.name + bcolors.ENDC)
					types[lr[1]] += 1
					slots[lr[5]] += 1
					allslots[lr[5]] += 1
					cost += cost_dict[lr[3]]
					count += 1
		print()
		print(bcolors.BOLD + "Slots: " + bcolors.ENDC, end="")
		pprint.pprint(dict(slots))
		print(bcolors.BOLD + "Types: " + bcolors.ENDC)
		pprint.pprint(dict(types))
		# To append dict types in sumtypes
		for t in types:
			if t in sumtypes:
				sumtypes[t].append(types[t])
			else:
				if s == "SOLD":
					sumtypes[t] = [0, types[t]]
				else:
					sumtypes[t] = [types[t]]
		print(bcolors.BOLD + "Count: " + bcolors.ENDC + str(count))
		print(bcolors.BOLD + "Cost: " + bcolors.ENDC + f'{cost:,} ' + "Mana")
		costs += cost
		total += count
		print("===========================================================================================================")
	print(bcolors.BOLD + "Total: " + bcolors.ENDC + str(total))
	print(bcolors.BOLD + "Total Cost: " + bcolors.ENDC + f'{costs:,} ' + "Mana")
	print(bcolors.BOLD + "Slots: " + bcolors.ENDC, end="")
	pprint.pprint(dict(allslots))
	print(bcolors.BOLD + "Total types: " + bcolors.ENDC)
	pprint.pprint(sumtypes)


if __name__ == "__main__":
	main()
