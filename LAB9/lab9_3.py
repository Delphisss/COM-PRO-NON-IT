import random
from basic_stats import average, std
# import basic_stats as stat
def simulate_dice_rolls(num_rolls):
    rolls = [random.randint(1, 6) for _ in range(num_rolls)]
    return rolls

def count_(rolls):
    Occ = {i: rolls.count(i) for i in range(1, 7)}
    return Occ

num_rolls = 2000
dice_rolls = simulate_dice_rolls(num_rolls)
Occ = count_(dice_rolls)

print("Simulation of 2,000 dice rolls")
print("Face Occurrence")

for face, count in Occ.items():
    print(f"{face}    {count}")

avg = average(dice_rolls)
std_dev = std(dice_rolls)

print(f"\nAverage = {avg:.2f}")
print(f"Standard deviation = {std_dev:.2f}")

