Array = [1,2,3,4,5,6]

print(Array)
m = int(input("Please input the first index: "))
n = int(input("Please input the second index: "))
print("Before swapping: ")
print(Array)
temp = Array[m]
Array[m] = Array[n]
Array[n] = temp
print("After swapping")
print(Array)