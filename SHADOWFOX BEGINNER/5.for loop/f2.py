'''
2. Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks,

"Are you tired?"

If you reply "yes" or "y,

" it should ask if you want to skip the remaining sets.

If you reply "yes" or "y,

" it should break and print,

"You completed a total of

jumping jacks.
"

For example, if you did only 30 jumping jacks and answered "yes,

" the program

will break and print,

"You completed a total of 30 jumping jacks.
"

If you reply "no" or "n,

" it should continue and display how many jumping jacks

are remaining. After that, ask you again,

"Are you tired?"

For example, if you answered "no,

" it should display that 70 jumping jacks are

remaining and ask you again,

"Are you tired?"

If you reply "no" or "n,

" it should continue and display how many jumping jacks

are remaining. After that, ask you again,

"Are you tired?"

For example, if you answered "no,

" it should display that 70 jumping jacks are

remaining and ask you again,

"Are you tired?"

If you complete all 100 jumping jacks, it should print,

"Congratulations! You

completed the workout,

" and stop the program
'''
total = 0

for i in range(10):
    total = total + 10

    print("You completed", total, "jumping jacks.")

    if total == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? ")

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? ")

        if skip == "yes" or skip == "y":
            print("You completed a total of", total, "jumping jacks.")
            break

    remaining = 100 - total
    print(remaining, "jumping jacks remaining.")