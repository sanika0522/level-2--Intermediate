import json

def load_tasks(filename='tasks.json'):
         try:
             with open(filename, 'r') as file:
                 return json.load(file)
         except FileNotFoundError:
             return []

def save_tasks(tasks, filename='tasks.json'):
         with open(filename, 'w') as file:
             json.dump(tasks, file)

def add_task(tasks, task):
         tasks.append({'task': task, 'done': False})
         save_tasks(tasks)

def list_tasks(tasks):
         for index, task in enumerate(tasks):
             status = "✓" if task['done'] else "✗"
             print(f"{index + 1}. [{status}] {task['task']}")

tasks = load_tasks()
while True:
         action = input("Choose an action: add, list, quit: ")
         if action == 'add':
             task = input("Enter a task: ")
             add_task(tasks, task)
         elif action == 'list':
             list_tasks(tasks)
         elif action == 'quit':
             break
         else:
             print("Invalid action.")
     