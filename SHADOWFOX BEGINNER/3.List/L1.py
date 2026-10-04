'''
3. List
1. You have a list of superheroes representing the Justice League. justice_league =
["Superman"
,
"Batman"
,
"Wonder Woman"
,
"Flash"
,
"Aquaman"
,
"Green

Lantern"]
Perform the following tasks:
1. Calculate the number of members in the Justice League.
2. Batman recruited Batgirl and Nightwing as new members. Add them to your
list.
3. Wonder Woman is now the leader of the Justice League. Move her to the
beginning of the list.
4. Aquaman and Flash are having conflicts, and you need to separate them.
Choose either "Green Lantern" or "Superman" and move them in between
Aquaman and Flash.
5. The Justice League faced a crisis, and Superman decided to assemble a new
team. Replace the existing list with the following new members: "Cyborg"
,

"Shazam"
,
"Hawkgirl"
,
"Martian Manhunter"
,
"Green Arrow"
.

6. Sort the Justice League alphabetically. The hero at the 0th index will become
the new leader.

(BONUS: Can you predict who the new leader will be?)

Your task is to write Python code to perform these operations on the
"justice_league" list. Display the list at each step to observe the changes.
'''
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding new members:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After changing the leader:", justice_league)

# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

# 5. Replace the list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League:", justice_league)

# 6. Sort the list alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)

# Display the new leader
print("New Leader:", justice_league[0])