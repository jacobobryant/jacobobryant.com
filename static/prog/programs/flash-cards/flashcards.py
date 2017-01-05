import random

# read packs, terms and definitions from a text file
with open("data.txt", "r") as f:
    text = f.read()

# parse the packs
packs = []
for block in text.strip().split('\n\n'):
    lines = block.split('\n')
    title = lines[0]
    
    # parse the terms and definitions
    terms = {}
    for line in lines[1:]:
        term, definition = line.split(':', 1)
        terms[term.strip()] = definition.strip()

    packs.append({"title": title, "terms": terms})

# select a pack
print("Packs to choose from:")
for i, pack in enumerate(packs):
    print(i, "-", pack["title"])
choice = int(input("Enter a number from 0 to {}: "
                   .format(len(packs) - 1)))
pack = packs[choice]["terms"]

# quiz the user on each term in the pack
terms = list(pack.keys())
random.shuffle(terms)
for term in terms:
    print()
    input("Think of the definition of \"{}\", "
          "then press Enter".format(term))
    print("The definition is \"{}\"".format(pack[term]))
