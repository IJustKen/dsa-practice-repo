#Given an array of integers arr[]. Find the Inversion Count in the array.
#Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

#Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.


arr = [2, 4, 1, 3, 5]

#First I use brute force which is n^2 cuz we see every possible pair
#Then I thought could we somehow count the inversions during mergesort so that we get nlogn complexity
#Logic is when we split into two parts left and right, there are inversions within left half and inversions within right half. 
#then there are also inversions between the two halves, if something in left side is greater than the thing in right, that is also inversion no
#Now if left and right are sorted that means if left something is bigger than thing on right, all following elem in left will also be
#bigger and thus inversions with the current a2[j]. So we add full directly.

def merge(a1,a2):
    i,j = 0,0
    res = []
    count = 0
    while i<len(a1) and j<len(a1):
        if a1[i] <= a2[j]:
            res.append(a1[i])
            i += 1
        elif a2[j] < a1[i]:
            res.append(a2[j])
            j += 1
            count += len(a1) - i
    res.extend(a1[i:])
    res.extend(a2[j:])
    return res, count

def mergesort(a1):
    if len(a1) <= 1:
        return a1, 0
    mid = (len(a1))//2
    left, left_half_inversions = mergesort(a1[:mid])
    right, right_half_inversions = mergesort(a1[mid:])
    final, left_and_right_halves_inversions = merge(left,right)

    return final, left_and_right_halves_inversions + left_half_inversions + right_half_inversions


    

print(mergesort(arr))