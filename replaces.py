import re

to_replace = {
    "From": "from",
    "Guide To": "Guideto",
    "Of": "of",
    "of The": "ofthe",
    "of A ": "ofa"
}

path = input("Path of filename: ")

# Read
fin = open(path, "rt")
data = fin.read()
#replace all occurrences of the required string
for word in to_replace:
    data = re.sub('([A-Z])', r' \1', data)
    data = data.replace(word, to_replace[word])
    data = data.replace(" ", "")
fin.close()

# Write
fin = open(path, "wt")
#overrite the input file with the resulting data
fin.write(data)
fin.close()