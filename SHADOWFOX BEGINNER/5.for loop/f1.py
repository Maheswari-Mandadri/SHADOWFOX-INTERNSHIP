'''
1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row
'''
import random

six_count = 0
one_count = 0
two_sixes = 0
previous = 0

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll", i + 1, ":", roll)

    if roll == 6:
        six_count += 1

    if roll == 1:
        one_count += 1

    if roll == 6 and previous == 6:
        two_sixes += 1

    previous = roll

print("Output: Number of times rolled 6:", six_count)
print("Output: Number of times rolled 1:", one_count)
print("Output: Number of times rolled two 6s in a row:", two_sixes)