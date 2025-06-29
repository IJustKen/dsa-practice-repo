arr = [3,6,6,2,5,1]

for i in range(len(arr)):
    if i == 0:
        continue
    j = i-1
    key = arr[i]
    while j >= 0 and key < arr[j]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        j -= 1

print(arr)