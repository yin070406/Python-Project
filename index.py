Array = []

def push():
    InputData = input("Please enter your data: ")
    Array.append(InputData)

def pop():
    DeleteData = int(input("Please enter the data you want to delete: "))
    Array.pop(DeleteData)

def Display():
    print(Array)

while True:
    print("1 - Push")
    print("2 - Pop")
    print("3 - Display")
    print("0 - Exit")

    num = int(input("Please enter your choice: "))

    if (num == 1):
        push()
    elif (num == 2):
        pop()
    elif (num == 3):
        Display()
    elif (num == 0):
        break