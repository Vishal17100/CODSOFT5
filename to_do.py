# To-Do List Program

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    index = int(input("Enter task number to update: ")) - 1
    task = input("Enter updated task: ")
    tasks[index] = task
    print("Task updated successfully!")

def delete_task():
    index = int(input("Enter task number to delete: ")) - 1
    del tasks[index]
    print("Task deleted successfully!")

while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")