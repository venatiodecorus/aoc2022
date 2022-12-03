import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

# Part one
total = 0
for pack in lines:
    sack1 = pack[0:len(pack)//2]
    sack2 = pack[len(pack)//2 if len(pack)%2 == 0 else ((len(pack)//2)+1):]
    same = ''.join(sorted(set.intersection(set(sack1), set(sack2))))
    c = 0
    if same.islower():
        c = ord(same) - 96
    else:
        c = ord(same) - 65 + 27
    total += c
print(total)

# Part Two
total = 0
group = []
for pack in lines:
    group.append(pack)
    if len(group) == 3:
        same = ''.join(sorted(set.intersection(set(group[0]), set(group[1]), set(group[2]))))
        c = 0
        if same.islower():
            c = ord(same) - 96
        else:
            c = ord(same) - 65 + 27
        total += c
        group = []
print(total)