import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

t = 0
t2 = 0
for l in lines:
    a,b = l.split(',')
    c,d = range(int(a.split('-')[0]), int(a.split('-')[1])), range(int(b.split('-')[0]), int(b.split('-')[1]))
    if (c.start <= d.start and c.stop >= d.stop) or (c.start >= d.start and c.stop <= d.stop):
        t += 1
    if c.start <= d.stop and d.start <= c.stop:
        t2 += 1
print(t)
print(t2)
