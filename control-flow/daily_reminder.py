task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"Reminder: {task} is a medium priority task. Try to complete it soon.")
    case "low":
        print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f" '{task}' has an unrecognized priority level.")

if time_bound == "yes":
    print(f"Reminder: {task} that requires immediate attention today!")
else:
    print(f"Note: {task}. Consider completing it when you have free time.")


            