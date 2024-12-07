import sys, json, time

if len(sys.argv) < 2:
    print("Invalid Input!")
    print("Usage: task-tracker [COMMAND] [ARGUMENTS]")
    sys.exit(1)

# Load data
try:
    file = open("data.json", "r")
    data = json.load(file)
    latest_id = data["latest_id"]
    tasks = data["tasks"]
except FileNotFoundError:
    tasks = []
    latest_id = 0

# Handling different operations
match sys.argv[1]:
    case "add":
        if len(sys.argv) < 3:
            print("Usage: task-tracker add [DESCRIPTION]")
            sys.exit(2)
        latest_id += 1
        tasks.append({
            "id": latest_id,
            "description": sys.argv[2],
            "status": "todo",
            "createdAt": time.time(),
            "modifiedAt": time.time()
        })
        print(f"Added task '{sys.argv[2]}' with ID {latest_id}")
    case "update":
        if len(sys.argv) < 4:
            print("Usage: task-tracker update [TASK_ID] [NEW_DESCRIPTION]")
            sys.exit(3)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("The task id must be numeric!")
            sys.exit(4)
        new_description = sys.argv[3]
        updated = False
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["modifiedAt"] = time.time()
                updated = True
        if not updated:
            print(f"ID {task_id} doesn't exist!")
        else:
            print(f"Task {task_id} updated to {new_description}")
    case "delete":
        if len(sys.argv) < 3:
            print("Usage: task-tracker delete [TASK_ID]")
            sys.exit(3)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("The task id must be numeric!")
            sys.exit(4)
        deleted = False
        for index, task in enumerate(tasks):
            if task["id"] == task_id:
                tasks.pop(index)
                print(f"Task {task_id}: '{task['description']}' deleted successfully")
                deleted = True
        if not deleted:
            print(f"ID {task_id} doesn't exist!")
    case "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task-tracker mark-in-progress [TASK_ID]")
            sys.exit(3)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("The task id must be numeric!")
            sys.exit(4)
        updated = False
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "in progress"
                print(f"Updated task (ID {task['id']}): '{task['description']}' to in progress.")
                updated = True
        if not updated:
            print(f"ID {task_id} doesn't exist!")
    case "mark-done":
        print("marking done")
    case "list":
        print("listing tasks")
    case _:
        print("Unknown command!")

# Saving the new data
file = open("data.json", "w")
json.dump({
    "latest_id": latest_id,
    "tasks": tasks
}, file, indent=4)