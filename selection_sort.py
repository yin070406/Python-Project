Array = [2,5,3,1,6,4]

print(f"Original Array: {Array}")
for i in range(0, len(Array)):
    max_index = i
    for j in range(i+1, len(Array)):
        if Array[j] > Array[max_index]:
            max_index = j
    temp = Array[i]
    Array[i] = Array[max_index]
    Array[max_index] = temp
print(f"New Array: {Array}")