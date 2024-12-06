import sys

if len(sys.argv) < 2:
    print("Invalid Input!")
    print("Usage: task-tracker [COMMAND] [ARGUMENTS]")
    sys.exit(1)

match sys.argv[1]:
    case "add":
        print("Adding a task")
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