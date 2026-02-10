todos = []

while True :

    choice = print('''
    Welcome to Todo app
         
    1. Add a task
    2. View tasks
    3. Edit task
    4. Complete a task
    5. Remove a task
    6. Exit the app  ''')
  
    choice =  input("Enter option: ")
    
    if choice == "1" :
        task = input("Enter new task : ")
        todos.append({"task": task, "status": "pending"})
        print(f"{task} added sucessfully")

    elif choice == "2" :
        if len(todos) == 0:
            print("No todos found, add todo")
        else :
            print('Your Todos')
            for i, todo in  enumerate(todos, start=1):
                print(f"{i}. {todo['task']} [{todo['status']}]")

    elif choice == "3":
        if len(todos) == 0:
            print("No todos found, add todo")
        else :
            print('Your Todos')
            for i, todo in  enumerate(todos, start=1):
                print(f"{i}. {todo['task']} [{todo['status']}]")
          
            i= int(input("Enter the task number you want to Edit: ")) -1
            if 0 <= i < len(todos):
                task = input("Enter new task : ")
                todos[i]["task"] = task
                print(f"{task} edited sucessfully")

    elif choice == "4":
        if len(todos) == 0:
            print("No todos found, add todo")
        else :
            print('Your Todos')
            for i, todo in  enumerate(todos, start=1):
                print(f"{i}. {todo['task']} [{todo['status']}]")
          
            i= int(input("Enter the task number you want to mark complete: ")) -1
            if 0 <= i < len(todos):
                todos[i]["status"] = "completed"
                print(f"'{todos[i]['task']}' marked as completed")

    elif choice == "5":
    
        if len(todos) == 0:
            print("No todos found, add todo")
        else :
            print('Your Todos')
            for i, todo in  enumerate(todos, start=1):
                print(f"{i}. {todo['task']} [{todo['status']}]")
          
            i= int(input("Enter the task number you want to remove: ")) -1
            if 0 <= i < len(todos) :
                final_task = todos.pop(i)
                print(f"'{final_task['task']}' removed sucessfully")

    elif choice == "6":
           break