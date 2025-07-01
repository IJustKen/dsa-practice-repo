import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = random.randint(0,len(arr)-1) 
    pivot = arr[pivot_idx]
    fin = False

    arr[-1],arr[pivot_idx] = arr[pivot_idx],arr[-1]
   
    while not fin:
        lp = 0
        rp = len(arr)-2
        for i in range(len(arr)-1):
            if arr[lp] > pivot:
                break
            else:
                lp += 1
        for i in range(len(arr)-1):
            if arr[rp] < pivot:
                break
            else:
                rp -= 1
        if lp > rp:
            arr[lp],arr[-1] = arr[-1],arr[lp]
            fin = True
        elif rp > lp:
            arr[lp],arr[rp] = arr[rp], arr[lp]

    return quicksort(arr[:lp]) + [pivot] + quicksort(arr[lp+1:])
    
print(quicksort([5,1,5,7,2,7]))


