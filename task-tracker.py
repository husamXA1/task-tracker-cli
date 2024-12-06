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
    case "update":
        print("updating a task")
    case "delete":
        print("deleting a task")
    case "mark-in-progress":
        print("marking in progress")
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