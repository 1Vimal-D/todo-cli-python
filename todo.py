import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def display_menu():
    print("\n===== TODO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added!")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                print("\nSelect task number to delete:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    idx = int(input("Enter task number: "))
                    if 1 <= idx <= len(tasks):
                        removed = tasks.pop(idx - 1)
                        save_tasks(tasks)
                        print(f"Deleted: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
