import numpy as np

score = 0

loses_to = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

def game(opp, me):
    if opp == loses_to[me]:
        return "win"
    if me == loses_to[opp]:
        return "lose"
    if opp == me:
        return "tie"

hand_shapes = { 
    "A": {"shape": "Rock", "points": 1},
    "B": {"shape": "Paper", "points": 2},
    "C": {"shape": "Scissors", "points": 3},
    "X": {"shape": "Rock", "points": 1},
    "Y": {"shape": "Paper", "points": 2},
    "Z": {"shape": "Scissors", "points": 3} 
    }

points = {
    "lose": 0,
    "tie": 3,
    "win": 6 
}

with open('input.txt') as f:
    rounds = np.loadtxt(f, dtype='U', delimiter=' ')

for r in rounds:
    opp = hand_shapes[r[0]]['shape']
    me = hand_shapes[r[1]]['shape']
    shape_score = hand_shapes[r[1]]['points']
    outcome = game(opp, me)
    outcome_score = points[outcome]
    total_score = shape_score + outcome_score
    score += total_score

print(score)
