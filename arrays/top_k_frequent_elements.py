#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:

    #bucket sort approach. Make a list of independent lists. Basically we make buckets in this way - each bucket represents a frequency
    #the values in the bucket are numbers with that frequency
    #so first we get the counts and then prepare our buckets
    #after that we iterate from the back of the bucket list to get the k most frequent nums

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_vs_nums = [[] for _ in range(len(nums))]      #dont do [[]]*len this creates len dependent lists(they all are the same)
        counts = DefaultDict(int)       
        for num in nums:
            counts[num] += 1
        for n,f in counts.items():
            frequency_vs_nums[f-1].append(n)        #bucket ready
        rem = k
        ans = []
        for i in range(len(nums)-1,-1,-1):
            for num in frequency_vs_nums[i]:
                if rem == 0:
                    break
                ans.append(num)
                rem -= 1
            if rem == 0:
                break
        return ans




class Solution:

    #idea 1 - get a count of every number using dictionary and convert it to a list
    #then use a custom mergesort based on the idx 1 not 0.
    #this is nlogn

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = DefaultDict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
        counts_list = []
        for key,v in counts.items():
            counts_list.append([key,v])
        def merge(a1,a2):
            res = []
            i, j = 0,0
            while i < len(a1) and j <len(a2):
                if a1[i][1] < a2[j][1]:
                    res.append(a1[i])
                    i += 1
                elif a1[i][1] >= a2[j][1]:
                    res.append(a2[j])
                    j += 1
            res.extend(a1[i:])
            res.extend(a2[j:])

            return res
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            return merge(mergesort(arr[:mid]),mergesort(arr[mid:]))


        sorted_nums = mergesort(counts_list)[::-1]
        final = []
        for i in range(k):
            final.append(sorted_nums[i][0])
        return final
