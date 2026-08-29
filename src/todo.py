tasks = []



while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as complete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== YOUR TASKS =====")
            for i, task in enumerate(tasks, 1):
                if task["completed"]:
                    print(f"{i}. ✓ {task['name']}")
                else:
                    print(f"{i}. ○ {task['name']}")

    # Delete task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    # Mark task as complete
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")




