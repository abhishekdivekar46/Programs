queue = []

def enq():
    ele = int(input("Enter a element = "))
    queue.append(ele)
    print("Enqueued = ",ele)

def deq():
    if len(queue) == 0:
        print("Empty queue")
    else:
        ele = queue.pop(0)
    print("Dequeued ",ele)    

def display():
    print("queue is ",queue)

def empty():
    n = len(queue)
    for i in range(n):
        queue.pop()

while True:
    op = int(input("1.ENQUEUE 2.DEQUEUE 3.DISPLAY 4.EMPTY 5.QUIT  "))
    if op == 1:
        enq()
    elif op == 2:
        deq()
    elif op == 3:
        display()
    elif op == 4:
        empty()

    elif op == 5:
        break
    else:
        print("Invalid Option")                

