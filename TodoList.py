# To-Do List - By Youssef Khaled
tasks = []
print("=== To-Do List ===")

while True:
    task = input("Enter task (or 'exit' to quit): ")
    if task == "exit":
        break
    tasks.append(task)
    print("Tasks:", tasks)