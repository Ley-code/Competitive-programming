class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        length = len(instructions)
        arr = [[0]*2 for i in range(length)]
        def merge(left_arr,right_arr):
            nonlocal arr
            n,m = len(left_arr),len(right_arr)
            l  = r = 0
            prevleft = 0
            prevright = 0
            while r<m:
                if r>0 and instructions[right_arr[r]]==instructions[right_arr[r-1]]:
                    arr[right_arr[r]][0] += prevleft
                    arr[right_arr[r]][1] += prevright
                else:
                    while l<n and instructions[right_arr[r]]>instructions[left_arr[l]]:
                        l+=1
                    arr[right_arr[r]][0] += l
                    prevleft = l
                    while l<n and instructions[right_arr[r]]==instructions[left_arr[l]]:
                        l+=1
                    arr[right_arr[r]][1] += n-l
                    prevright = n-l
                r+=1
            l = r = 0
            merged = []
            while l<n and r<m:
                if instructions[left_arr[l]]<instructions[right_arr[r]]:
                    merged.append(left_arr[l])
                    l+=1
                else:
                    merged.append(right_arr[r])
                    r+=1
            merged.extend(left_arr[l:])
            merged.extend(right_arr[r:])
            return merged
        def mergesort(l,r,nums):
            if l==r:
                return [l]
            mid = l + (r-l)//2
            left = mergesort(l,mid,nums)
            right = mergesort(mid+1,r,nums)
            return merge(left,right)
        mergesort(0,length-1,instructions)
        sums = 0
        for i in range(length):
            sums += min(arr[i][0],arr[i][1])
        sums = sums % (10**9+7)
        return sums
        

        