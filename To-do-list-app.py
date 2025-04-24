tasks = []

while True:
    print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet")
    elif choice == "3":
        if tasks:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid number")
        else:
            print("No tasks to remove")
    elif choice == "4":
        print("Goodbye")
        break