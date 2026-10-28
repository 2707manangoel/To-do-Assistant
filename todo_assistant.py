tasks =[]

def add_task():
    task_name =input("Enter a new task: ").strip()
    if task_name:
        tasks.append({
            "name": task_name,
            "completed": False
        })
        print("Task added successfully!")
    else:
        print("Task name cannot be empty.")

def view_tasks():
    if not tasks:
        print("Your task list is empty.")
        return
    print("\n --- Your Tasks ---")
    for number, task in enumerate(tasks,start =1):
        if task["completed"]:
            status ="Completed"
        else:
            status="Pending"
        print(f"{number}.{task['name']}-{status}")

def complete_task():
    view_tasks()
    if not tasks():
        return
    try:
        number = int(input("Enter the task number to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number-1]["completed"]=True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n =====SMART TO-DO ASSISTANT ======")
        print("1. Add task")
        print("2. View task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice =="2":
            view_tasks()
        elif choice =="3":
            complete_task()
        elif choice =="4":
            print("Goodbye! Keep making progress.")
            break

        else:
            print("Invalid choice. Choose from 1 to 4.")

if __name__ == "__main__":
    main()
     