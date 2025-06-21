from TaskManager import TaskManager

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'taskdb'
}

def help_menu():
    print("""
    Commands:
      add       -> Add a new task with title, description, due date, and priority
      list      -> View all tasks (can optionally filter by status or priority)
      update    -> Update a task's details using its ID
      done      -> Mark a task as completed using its ID
      delete    -> Delete a task using its ID
      help      -> Show this help menu
      exit      -> Exit program
    """)

def prompt_input():
        print("\nWhat do you want to do?")
        print("- add")
        print("- list")
        print("- update")
        print("- done")
        print("- delete")
        print("- help")
        print("- exit")
        return input("Enter command: ").strip().lower()
    
def main():
    manager = TaskManager(DB_CONFIG)

    while True:
        cmd = prompt_input()

        if cmd == "add":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (Low, Medium, High): ")
            manager.add_task(title, desc, due, priority)

        elif cmd == "list":
            print("Enter optional filters (press Enter to skip):")
            status = input("Status (Pending/Completed): ").strip() or None
            priority = input("Priority: ").strip() or None
            filters = {}
            if status:
                filters["status"] = status
            if priority:
                filters["priority"] = priority
            manager.list_tasks(**filters)

        elif cmd == "update":
            task_id = input("Task ID to update: ")
            print("Enter new values (press Enter to skip):")
            title = input("New title: ").strip()
            desc = input("New description: ").strip()
            due = input("New due date (YYYY-MM-DD): ").strip()
            priority = input("New priority: ").strip()
            status = input("New status (Pending/Completed): ").strip()
            updates = {}
            if title:
                updates["title"] = title
            if desc:
                updates["description"] = desc
            if due:
                updates["due_date"] = due
            if priority:
                updates["priority"] = priority
            if status:
                updates["status"] = status
            if updates:
                manager.update_task(int(task_id), **updates)
            else:
                print("No updates provided.")

        elif cmd == "done":
            task_id = input("Task ID to mark as completed: ")
            manager.mark_completed(int(task_id))

        elif cmd == "delete":
            task_id = input("Task ID to delete: ")
            manager.delete_task(int(task_id))
    
        elif cmd == "help":
            help_menu()
    
        elif cmd == "exit":
            print("Program terminated.")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
