from prettytable import PrettyTable
# file = open("tasks.txt")
tasks = []
# for line in file:
#     tasks.append(line.strip())
def print_menu():
    print("""What would you like to do?
1. Add a task
2. List tasks
3. Mark a task as done
4. Quit""")
          

def add_task():
    valid_priority = ["high", "low", "med"]
    task = input("Enter a task title: ")
    description = input('Enter a task description: ')
    priority = input('Enter a task priority: (High|Low|Med) ').lower()
    while priority not in valid_priority:
        priority = input('Enter a task priority: (High|Low|Med) ').lower()
    task_dict = {
        "title": task,
        "description": description,
        "priority": priority,
        "status": "Not Done"
    }
    tasks.append(task_dict)
    # file.write(tasks)
    print(task_dict)
    return task_dict


def print_tasks():
    x = PrettyTable()
    x.field_names = ["Index", "Title", "Description", "Priority", "Status"]
    for i in range(0,len(tasks)):
        x.add_row([i+1 ,tasks[i]['title'], tasks[i]['description'], tasks[i]['priority'], tasks[i]['status']])
    print(x)


def mark_task_as_done():
    print_tasks()
    num = input("Enter a task number: ")
    num = int(num) -1
    tasks [num] ['status'] = 'Done'
    current_title = tasks[num]['title']
    print(f'{current_title} has been marked as Done')
    print_tasks()

    
def main():
    print_menu()
    user_input = input("Enter a number: ").lower().strip()
    print()
    while user_input != "4":
        if user_input == "1":
            add_task()
            print()
        elif user_input == '2':
            print_tasks()
            print()
        elif user_input == '3':
            mark_task_as_done()
            print()
        print_menu()
        user_input = input("Enter a number: ").lower().strip()
if __name__ == "__main__":
    main()