def main():
    tasks = []
    task_id = 1

    print("--- To-Do List Application ---")
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            task_name = input("Enter task: ").strip()
            
            if task_name:
                # appending task as a dictionary
                new_task = {
                    "id": task_id,
                    "task": task_name
                }
                tasks.append(new_task)
                print(f"Task added successfully! (ID: {task_id})")
                task_id += 1
            else:
                print("Task cannot be empty.")
                
        elif choice == '2':
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nYour Tasks:")
                print(f"{'ID':<5} | {'Task'}")
                print("-" * 25)
                for t in tasks:
                    print(f"{t['id']:<5} | {t['task']}")
                    
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()