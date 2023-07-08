stack = []

def push():
    ele = int(input("Enter a element = "))
    stack.append(ele)
    print("Pushed = ",ele)

def pop():
    if len(stack) == 0:
        print("Empty stack")
    else:
        ele = stack.pop()
    print("Popped ",ele)    

def display():
    print("stack is ",stack)

def empty():
    stack.clear()

def exit():
    quit()

menu_options = {
    '1' : push,
    '2' : pop,
    '3' : display,
    '4' : empty,
    '5' : exit
}

while True:
    print("1. Push")    
    print("2. Pop") 
    print("3. View") 
    print("4. Empty") 
    print("5. Exit")

    choice = input("Enter the choice: ")

    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid Choice")    












'''choice = int(input("1.Push 2.Pop 3.Display 4.Empty 5.Quit  "))

match choice:

    case 1:    
        push()

    case 2:
        pop() 

    case 3:
        display()

    case 4:
        empty()'''

          

"""choice = int(input("1.Push 2.Pop 3.Display 4.Empty 5.Quit  "))

operations = [push, pop, display, empty]

output = operations[choice - 1]()
    
(output)"""
"""  if op == 1:
        push()
    elif op == 2:
        pop()
    elif op == 3:
        display()
    elif op == 4:
        empty()

    elif op == 5:
        break
    else:
        print("Invalid Option")      """          

