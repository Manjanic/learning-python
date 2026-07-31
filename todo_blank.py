import json
import os
def load_tasks():
    if os.path.exists("tasks.json"):
          with open("tasks.json","r") as file:
            return json.load(file)
    else:
        return []

def add_task(tasks):
    name = input("Name task: ")
    tasks.append({"name":name, "done":False})
    print(f"{name}  added")
def view_tasks(tasks):
    if not tasks:
       print("No task yet")
       return
    for i, task in enumerate(tasks,1):
        status= "[DONE]" if task['done'] else "[PENDING]"
        print(f"{i}. {status} {task['name']}")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Which to delete ?: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid number")
    except ValueError:
        print("Please type a number")
def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=2)
def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(print("Which ?: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            print("Marked done!")
        else:
            print("Invalid number. ")
    except ValueError:
        print("Please type a number ")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List ===")
        print("1: Add task")
        print("2: view task")
        print("3: Mark task")
        print("4: Delete task")
        print("5: Quit")

        choice = input("choose (1-5): ")
        if choice == "1":
            add_task(tasks)
        elif choice =="2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saved Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()