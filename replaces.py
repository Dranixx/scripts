import re
import json
import os
import sys

import sw.s2us

to_replace = {
    "From": "from",
    "Guide To": "Guideto",
    "Of": "of",
    "of The": "ofthe",
    "of A ": "ofa"
}

# Path of the file to modify
path = sys.argv[1]

def replace_from_dict(f):
    data = f.read()
    #replace all occurrences of the required string
    for word in to_replace:
        data = re.sub('([A-Z])', r' \1', data)
        data = data.replace(word, to_replace[word])
        data = data.replace(" ", "")
    return data

def replace_json(f):
    data = json.load(f)
    data = sw.s2us.decode_name(data)
    data = sw.s2us.change_eff(data)
    #data = sw.s2us.change_type(data, "Attack", "Shield", 1)
    data = sw.s2us.encode_name(data)

    return data

def main():
    # Read
    f = open(path, "rt")
    data = replace_json(f)
    f.close()

    # Write
    f = open(path, "wt")
    #overrite the input file with the resulting data 
    #f.write(data)
    json.dump(data, f, indent=4)
    f.close()

if __name__ == "__main__":
	main()