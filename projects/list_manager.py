#DM class Shopping List Manager
#so confused please help meee

a_list = []
while True:
    action = input( "what do you want to do\n 1.add task\n 2.remove task\n 3.show list\n 4.exit\n")    
    if action == "1":
        task = input ("what task do you want to add ")
        a_list.append(task)
        print ("your task has been added")
    elif action == "2":
        task = input("what task do you want removed")
        if task in a_list
    elif action == "4":
        break     