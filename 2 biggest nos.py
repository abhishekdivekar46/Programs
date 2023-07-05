
list = []

def two_largest_num(numbers):

    largest = 0
    second_largest = 0


    num = int(input("Enter number of elements in list: "))


    for i in range(1, num + 1):
       ele = int(input("Enter elements: "))
       list.append(ele)
       
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num   
    
    return largest, second_largest

largest, second_largest = two_largest_num(list)        

print("Largest element is:", largest)
print("Second Largest element is:", second_largest)


