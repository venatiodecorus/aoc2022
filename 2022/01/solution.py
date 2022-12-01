import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

elves = []
total = 0

for line in lines:
    if len(line) == 0:
        elves.append(total)
        total = 0
        continue
    total += int(line)

elves = sorted(elves)
print(elves[-1])
print(elves[-1] + elves[-2] + elves[-3])