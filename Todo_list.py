tasks=[]
def show_menu():
    print("\ntodo list menu")
    print("1. add task")
    print("2. remove task")
    print("3. view tasks")
    print("4. exit")
def add_task():
    task=input("Enter the task:")
    tasks.append(task)
    print("Task added succesfully")
def remove_task():
    view_tasks()
    try:
        task_index=int(input("Enter the task number you want to remove")) -1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"task {removed_task} removed")
        else:
            print("invalid task number")
    except ValueError:
        print("invalid  input. please enter a number")
def view_tasks():
    if tasks:
        print("\nYour tasks ")
        for i,j in enumerate(tasks,start=1):
            print(f"{i}. {j}")
    else:
        print("No task found :(")
def main():
    while True:
        show_menu()
        choice=input("Chose an option between 1-4")
        if choice=="1":
            add_task()
        elif choice=="2":
            remove_task()
        elif choice=="3":
            view_tasks()
        elif choice=="4":
            print("Exiting the program")
            break
if __name__ == "__main__":
    main()
