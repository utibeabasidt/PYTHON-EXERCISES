todo_list = ['cook dinner', 'wash clothes']
is_app_running = True

'''Function to loop over the todo list'''
def view_list(): 
  print('TODO LIST')
  count = 1
  for each_todo in todo_list:
    print(f'{count}:  {each_todo}')
    count += 1

'''Function to add a todo to the list'''
def add_todo(): 
  todo = input('What do you want to do: ')
  todo_list.append(todo)
  print('Todo added successfully')

'''Funtion to delete a todo using the index of that todo, and also checking for Exception Error'''
def delete_todo(): 
  is_user_choice_invalid = True
  while is_user_choice_invalid:
    view_list()
    user_choice = int(input(f'What number do you want to remove from 1 to {len(todo_list)}: '))
    try:
      for i in range(0, len(todo_list)):
        if i + 1 == user_choice:
          todo_list.remove(todo_list[i])
      print('Deleted successfully')
      is_user_choice_invalid = False
    except KeyError:
      print('Value is not on the list.')

'''Displaying prompts and redirecting to each function'''
while is_app_running:
  print()
  print('''WELCOME TO YOUR TODO LIST PROGRAM
      1. VIEW TODO LISTS
      2. ADD A TODO 
      3. DELETE A TODO
      4. EXIT''')
  user_choice = int(input('Enter an option from 1-4: '))
  match (user_choice):
    case 1:
      view_list()
    case 2:
      add_todo()
    case 3:
      delete_todo()
    case 4:
      print('Program terminated')
      is_app_running = False
    case _:
      print('Incorrect input.')