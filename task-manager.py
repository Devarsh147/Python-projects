tasks = []

def show_tasks():
    print("Your Tasks: ")
    for i ,task in enumerate(tasks,1):
        print(f"{i}.{task}")


while True:
    print("Option 1-add | 2-view task | 3-Exit")
    choice = input("Enter choice: ")

    if choice =="1":
        task = input("Enter task: ")
        tasks.append(task)
        print("task added")
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("bye")
        break
    else:
        print("Invaild choice: ")