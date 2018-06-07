#!/usr/bin/python3

import os

with open("wordslist.txt", "r") as fh:
    subdomains = list(filter(bool, fh.read().split()))

prefixs = ["", "au02", "au03", "pre", "post", "non"]
suffixes = ["", "ing", "ment"]

for line in open("perms.txt", "r"):
    prefixs.append(line.strip().lower())
    suffixes.append(line.strip().lower())

print(prefixs)
print(suffixes)

generated = []

for d in subdomains:
    for p in prefixs:
        generated += [p + d]
        if p == "" or d == "":
            continue
        generated += [p + "-" + d]
    for s in suffixes:
        generated += [d + s]
        if d == "" or s == "":
            continue
        generated += [d + "-" + s]

subdomains += generated

subdomains = sorted(subdomains)

with open("permutations_untouched.txt", "w") as fh:
    fh.write("\n".join(subdomains))

os.system("sort permutations_untouched.txt | uniq permutations_untouched.txt > permutations.txt")
print("Deleting previous split folder")
os.system("rm -rf splits")
os.system("rm -rf results")
print("Making split folder")
os.system("mkdir splits")
os.system("mkdir results")
print("Splitting permutations.txt")
os.system("split -n 100 -d permutations.txt splits/")
print("Deleting permutations.txt")
os.system("rm permutations.txt")
os.system("rm permutations_untouched.txt")
