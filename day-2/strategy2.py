import numpy as np

score = 0

rules = {
    "Rock": {"beaten_by": "Paper", "beats": "Scissors", "ties": "Rock", "id": "A"},
    "Paper": {"beaten_by": "Scissors", "beats": "Rock", "ties": "Paper", "id": "B"},
    "Scissors": {"beaten_by": "Rock", "beats": "Paper", "ties": "Scissors", "id": "C"}
}

hand_shapes = { 
    "A": {"shape": "Rock", "points": 1},
    "B": {"shape": "Paper", "points": 2},
    "C": {"shape": "Scissors", "points": 3}
    }

outcomes = {
    "X": {"outcome": "lose", "points": 0},
    "Y": {"outcome": "tie", "points": 3},
    "Z": {"outcome": "win", "points": 6} 
}

def choice(opp, outcome):
    if outcome == "win":
        return rules[opp]["beaten_by"]
    if outcome == "lose":
        return rules[opp]["beats"]
    if outcome == "tie":
        return rules[opp]["ties"]

with open('input.txt') as f:
    rounds = np.loadtxt(f, dtype='U', delimiter=' ')

for r in rounds:
    opp = hand_shapes[r[0]]["shape"]
    outcome = outcomes[r[1]]["outcome"]
    outcome_score = outcomes[r[1]]["points"]
    my_choice = choice(opp, outcome)
    identifier = rules[my_choice]["id"]
    choice_score = hand_shapes[identifier]["points"]
    total_score = outcome_score + choice_score
    score += total_score

print(score)