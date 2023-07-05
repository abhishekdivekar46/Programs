stack = []

def enq():
    ele = int(input("Enter a element = "))
    stack.append(ele)
    print("Enstackd = ",ele)

def deq():
    if len(stack) == 0:
        print("Empty stack")
    else:
        ele = stack.pop(0)
    print("DEstackD ",ele)    

def display():
    print("stack is ",stack)

def empty():
    n = len(stack)
    for i in range(n):
        stack.pop()

while True:
    op = int(input("1.ENstack 2.DEstack 3.displayPLAY 4.EMPTY 5.QUIT  "))
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

