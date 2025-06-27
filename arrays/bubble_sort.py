arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

swap_flag = True        #to check if any swapping happened. If there was no swapping it means list sorted already no
n = len(arr)

while swap_flag:        #sort until no swaps - that is list sorted

    swap_flag = False       #default false unless we see swap
    for x in range(1,n):        #n is initially full list
        if arr[x] < arr[x-1]:
            arr[x],arr[x-1] = arr[x-1],arr[x]
            swap_flag = True
    
    n -= 1          #after full swap, the last element is sorted, as in the largest number in the range we are scanning is in the end now
                    #here example - after 1st iteration 6 is at the end already, then second iter 4 is behind 6. So we dont need to scan till there
                    #hence reduce n also


print(arr)