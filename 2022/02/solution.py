import os

base_dir = os.path.realpath(os.path.dirname(__file__))
with open(base_dir + "/input.txt", "r") as file:
    input = file.read().rstrip()

lines = input.split("\n")

# Part One
score = 0
for line in lines:
    plays = line.split(" ")
    if plays[1] == 'X': # Rock
        score += 1
        if plays[0] == 'C':
            score += 6
        elif plays[0] == 'A':
            score += 3
    elif plays[1] == 'Y': # Paper
        score += 2
        if plays[0] == 'A':
            score += 6
        elif plays[0] == 'B':
            score += 3
    elif plays[1] == 'Z': # Scissors
        score += 3
        if plays[0] == 'B':
            score += 6
        elif plays[0] == 'C':
            score += 3
print(score)

# Part Two
score2 = 0
for line in lines:
    plays = line.split(" ")
    # Rock
    if plays[0] == 'A':
        if plays[1] == 'X': # Lose
            score2 += 3
        elif plays[1] == 'Y': # Draw
            score2 += 3
            score2 += 1
        elif plays[1] == 'Z': # Win
            score2 += 6
            score2 += 2
    # Paper
    if plays[0] == 'B':
        if plays[1] == 'X': # Lose
            score2 += 1
        elif plays[1] == 'Y': # Draw
            score2 += 3
            score2 += 2
        elif plays[1] == 'Z': # Win
            score2 += 6
            score2 += 3
    # Scissors
    if plays[0] == 'C':
        if plays[1] == 'X': # Lose
            score2 += 2
        elif plays[1] == 'Y': # Draw
            score2 += 3
            score2 += 3
        elif plays[1] == 'Z': # Win
            score2 += 6
            score2 += 1
print(score2)