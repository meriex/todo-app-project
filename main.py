class TaskManager:
    def __init__(self):
        self.todos = []

    def add_task(self, task_name):
        self.todos.append({"task": task_name, "status": "pending"})
        return f"'{task_name}' added successfully!"

    def display_tasks(self):
        if not self.todos:
            print("\nNo todos found. Add one!")
            return False
        
        print("\n--- Your Todos ---")
        for i, todo in enumerate(self.todos, start=1):
            status = "✓" if todo["status"] == "completed" else " "
            print(f"{i}. [{status}] {todo['task']}")
        return True

    def edit_task(self, index, new_name):
        if 0 <= index - 1 < len(self.todos):
            self.todos[index - 1]["task"] = new_name
            return True
        return False

    def complete_task(self, index):
        if 0 <= index - 1 < len(self.todos):
            self.todos[index - 1]["status"] = "completed"
            return True
        return False

    def remove_task(self, index):
        if 0 <= index - 1 < len(self.todos):
            removed = self.todos.pop(index - 1)
            return removed["task"]
        return None

manager = TaskManager()

while True:
    print("\n1. Add | 2. View | 3. Edit | 4. Complete | 5. Remove | 6. Exit")
    choice = input("Enter option: ")

    if choice == "1":
        name = input("Task name: ")
        print(manager.add_task(name))

    elif choice == "2":
        manager.display_tasks()

    elif choice == "3":
        if manager.display_tasks():
            num = int(input("Task number to edit: "))
            new_name = input("New task name: ")
            if manager.edit_task(num, new_name):
                print("Edit successful!")
            else:
                print("Invalid number.")

    elif choice == "4":
        if manager.display_tasks():
            num = int(input("Task number to complete: "))
            if manager.complete_task(num):
                print("Task marked done!")
            else:
                print("Invalid number.")

    elif choice == "5":
        if manager.display_tasks():
            num = int(input("Task number to remove: "))
            task_name = manager.remove_task(num)
            if task_name:
                print(f"Removed: {task_name}")
            else:
                print("Invalid number.")

    elif choice == "6":
        print("Goodbye!")
        break