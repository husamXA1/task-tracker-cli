# Task Tracker CLI
This repo is a practice on [roadmap.sh](https://roadmap.sh/projects/task-tracker) task tracker cli project. It's a simple cli task tracking appplication where you can add, update, and delete tasks while tracking their stauts.

## How to use it
Using the app is simple. Just run it using Python and the tasks shall be saved in the ```data.json``` file.
```bash
python task-tracker.py add "Hello, World!"
#  Prints: Added task 'Hello, World!' with ID 1
```
## App Functionalities
The app has serveral functionalities as follows. When running the app each time, the data is loaded from the json file, the operation is applied on the tasks, and then saved again to the json file.
### Adding Tasks
You can add tasks as described in the previous example and give each task a description. A unique ID shall be assigned to each task (auto incremented for each new task).
### Updating Tasks
You can update a specific task based on its ID.
```bash
python task-tracker.py update 1 "New Description"
# Prints: Task 1 updated to 'New Description'
```
### Deleting Tasks
You can delete a specific task from the list based on its ID.
```bash
python task-tracker.py delete 1
# Prints: Task 1: 'New Description' deleted succesfully
```
### Setting Status
You can set the status of a specific task to ```in-progress``` or ```done```. The default status of a task is ```todo```.
```bash
python task-tracker.py mark-in-progress 5
# Sets the task of ID 5 to in-progress
python task-tracker.py mark-done 2
# Sets the task of ID 2 to done
```
### Viewing Tasks
You can view the list of all tasks or filter them based on their status.
```bash
python task-tracker.py list
# Lists all tasks

python task-tracker.py list todo
python task-tracker.py list in-progress
python task-tracker.py list done
# Lists tasks based on their status
```

## Colaboration
If you have any suggestion or improvement for the project, feel free to contact me on my email husamxm0@gmail.com or fork the project and submit a pull request with your changes.