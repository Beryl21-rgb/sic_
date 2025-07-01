import sys as s

# Implement Stack using list, insert and delete from rear of the list
# Implement Stack using list, insert and delete from front of the list
# Implement Queue using list, insert at rear delete from front the list
# Implement Queue using list, insert front, delete from rear of the list

# 1. Implement Stack using list, insert and delete from rear of the list
    
l = []
length = int(input("Enter the length of Stack: "))
        
def stack(choice):
    match(choice):
        case 1:
            if len(l) > length:
                print("Stack is full")
            else:
                input_value = int(input("Enter value to be pushed: "))
                l.append(input_value)
        case 2:
            if len(l) == 0:
                print("No element to pop")
            l.pop()
        case 3:
            if len(l) == 0:
                prnit("Stack is Emty")
                return
            else:
                print(l)
        case 4:
            s.exit("End of program")

        case _:
            print('Invalid choice')   
            
while True:
    print('1.Push  2.Pop  3.Display   4.exit')
    choice = int(input("Stack Operation: "))
    stack(choice)
    
    
    
    
# 2. Implement Stack using list, insert and delete from front of the list

l = []
length = int(input("Enter the length of Stack: "))
        
def stack(choice):
    match(choice):
        case 1:
            if len(l) > length:
                print("Stack is full")
            else:
                input_value = int(input("Enter value to be pushed: "))
                l.insert(0,input_value)
        case 2:
            if len(l) == 0:
                print("No element to pop")
            else:
                del l[0]
        case 3:
            if len(l) == 0:
                prnit("Stack is Emty")
                return
            else:
                print(l)
        case 4:
            s.exit("End of program")

        case _:
            print('Invalid choice')   
            
while True:
    print('1.Push  2.Pop  3.Display   4.exit')
    choice = int(input("Stack Operation: "))
    stack(choice)




# 3. Implement Queue using list, insert at rear delete from front the list

q = []
length = int(input("Enter the length of queue: "))
        
def queue(choice):
    match(choice):
        case 1:
            if len(q) >= length:
                print("Queue is full")
            else:
                input_value = int(input("Enter value to enque: "))
                q.append(input_value)
        case 2:
            if len(q) == 0:
                print("No element to deque")
            else:
                del q[0]
        case 3:
            if len(q) == 0:
                prnit("Queue is Emty")
                return
            else:
                print(q)
        case 4:
            s.exit("End of program")

        case _:
            print('Invalid choice')   
            
while True:
    print('1.Enque  2.Deque  3.Display   4.exit')
    choice = int(input("Stack Operation: "))
    queue(choice)
    
    
# 4. Implement Queue using list, insert front, delete from rear of the list

q = []
length = int(input("Enter the length of queue: "))
        
def queue(choice):
    match(choice):
        case 1:
            if len(q) >= length:
                print("Queue is full")
            else:
                input_value = int(input("Enter value to enque: "))
                q.insert(0,input_value)
        case 2:
            if len(q) == 0:
                print("No element to deque")
            else:
                q.pop()
        case 3:
            if len(q) == 0:
                prnit("Queue is Emty")
                return
            else:
                print(q)
        case 4:
            s.exit("End of program")

        case _:
            print('Invalid choice')   
            
while True:
    print('1.Enque  2.Deque  3.Display   4.exit')
    choice = int(input("Stack Operation: "))
    queue(choice)
