import random

groups = {
    "Italy": ["Estella", "Miki", "Jessica"],
    "Portugal": ["Shizhe", "Ben"], 
    "CostaRica": ["Nidhish", "Julius", "Jon", "Jay", "Eli"],
    "Japan": ["Emily"],
    "IDK": ["Harry"]
}

def attempt_assignment(pool):
    random.shuffle(pool)  # Randomize the pool for assignment
    assignments = {}  # Dictionary to store the assignments

    for i, (giver, giver_location) in enumerate(pool):
        for j in range(1, len(pool)):
            receiver_index = (i + j) % len(pool)
            receiver, receiver_location = pool[receiver_index]
            if giver_location != receiver_location and receiver not in assignments.values():
                assignments[giver] = receiver
                break

    return assignments

pool = [(person, location) for location, people in groups.items() for person in people]

max_attempts = 1000
for attempt in range(max_attempts):
    assignments = attempt_assignment(pool)
    if len(assignments) == len(pool):  # Check if everyone has been assigned
        break

if len(assignments) < len(pool):
    print("Failed to assign everyone a Secret Santa from a different location.")
else:
    for giver, receiver in assignments.items():
        print(f"{giver} -> {receiver}.")
