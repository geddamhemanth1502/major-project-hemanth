from task import Task
from file_handling import save_tasks, load_tasks

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{i + 1}. {task.title} ({task.category}) - {status}")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal, Urgent): ")
            tasks.append(Task(title, description, category))

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            task_id = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_id < len(tasks):
                tasks[task_id].mark_completed()
            else:
                print("Invalid task number.")

        elif choice == '4':
            display_tasks(tasks)
            task_id = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_id < len(tasks):
                tasks.pop(task_id)
            else:
                print("Invalid task number.")

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
