import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

stacks = [[],[],[],[],[],[],[],[],[]]
steps = []
m = []

s = False
for l in lines:
    if s:
        steps.append(l)
    else:
        m.append(l)
    if len(l) == 0:
        s = True
        continue;

for n in reversed(m[:-2]):
    f = n.replace('[','').replace(']','').replace('  ',' ')
    if f[0] != ' ': stacks[0].append(f[0])
    if f[2] != ' ': stacks[1].append(f[2])
    if f[4] != ' ': stacks[2].append(f[4])
    if f[6] != ' ': stacks[3].append(f[6])
    if f[8] != ' ': stacks[4].append(f[8])
    if f[10] != ' ': stacks[5].append(f[10])
    if f[12] != ' ': stacks[6].append(f[12])
    if f[14] != ' ': stacks[7].append(f[14])
    if f[16] != ' ': stacks[8].append(f[16])

print(stacks)
for s in steps:
    a = s.split(' ')
    count = a[1]
    src = int(a[3])-1
    dst = int(a[5])-1

    # Part Two
    b = stacks[src][len(stacks[src])-int(count):]
    stacks[src] = stacks[src][:-int(count)]
    stacks[dst].extend(b)

    # Part One
    # for _ in range(int(count)):
    #     b = stacks[src].pop()
    #     stacks[dst].append(b)

print(stacks)