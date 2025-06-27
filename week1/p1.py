# Check if the given input number is Even.

print("Enter a number to check if it is Even: ")
input_number = int(input)

if input_number % 2 == 0:
    print(input_number,'is an Even number')

# 1. Implement Stack using list, insert and delete from rear of the list

l = []
        
def stack(choice):
    match(choice):
        case 1:
            input_value = int(input("Enter value to be pushed: "))
            l.append(input_value)
        case 2:
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
