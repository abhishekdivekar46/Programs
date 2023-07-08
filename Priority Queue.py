queue = []

def enqueue():
    item = input("Enter the item: ")
    priority = int(input("Enter the priority:"))
    queue.append((item, priority))
    print("Enqueued successfully")

def dequeue():
    if len(queue) == 0:
        print("Empty Queue")
    else:
        priority_index = 0
        for i in range(1, len(queue)):
            if queue[i][1] < queue[priority_index][1]:
                priority_index = i
        print("Dequeued ", priority_index)
        return queue.pop(priority_index)[0]
    
        
    

def display():
    print("Queue is ", queue)

def empty():
    queue.clear()
    print("queue is cleared")

def exit():
    quit()

menu_options = {
    '1' : enqueue,
    '2' : dequeue,
    '3' : display,
    '4' : empty,
    '5' : exit
}

while True:
    print("1. Enqueue Item")    
    print("2. Dequeue Item") 
    print("3. View Queue") 
    print("4. Empty Queue") 
    print("5. Exit")

    choice = input("Enter the choice: ")

    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid Choice")    




