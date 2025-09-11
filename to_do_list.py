# Simple To-Do List in Python

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter the new task: ")
    tasks.append(task)
    print("Task added successfully!")

def mark_done():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                print(f"Task '{tasks[task_num]}' marked as done!")
                del tasks[task_num]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter task number to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"Task '{removed_task}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Remove a task")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
