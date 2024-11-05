import os

FILE_NAME = 'todo.txt'

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your TO-DO list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTO-DO List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            tasks = load_tasks()
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            tasks = load_tasks()
            display_tasks(tasks)
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
