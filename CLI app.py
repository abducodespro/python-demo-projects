# simple todo app

tasks = []

def show_menu():
    print("\n== TODO MENU ==")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("choose an option (2-4): ")

    if choice == "1":
        task = input("write your task: ")
        tasks.append(task)
        print("task added successfuly!")
    elif choice == "2":
        print("\nyour tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        index = int(input("enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"removed: {removed}")
        else:
            print("invalid task number!")
    elif choice == "4":
        print("goodbye")
        break
    else:
        print("invalid option")

