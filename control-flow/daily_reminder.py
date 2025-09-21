task = input("Enter your task for today: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

print(reminder)
