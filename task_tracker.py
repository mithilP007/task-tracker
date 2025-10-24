import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print(f"✅ Added task: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📝 No tasks found. Use 'add' to create one.")
        return
    print("\nYour Tasks:")
    print("-" * 40)
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t.get("completed") else "❌"
        print(f"{i}. {t.get('task')} [{status}]")
    print("-" * 40)

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print(f"🎉 Marked '{tasks[index]['task']}' as completed.")
    else:
        print("⚠️ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['task']}")
    else:
        print("⚠️ Invalid task number.")

def show_menu():
    print("\n=== 🧩 Task Tracker ===")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Complete Task")
    print("4️⃣  Delete Task")
    print("5️⃣  Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Task cannot be empty.")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            list_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
