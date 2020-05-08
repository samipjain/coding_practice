def nextGreaterElement(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return[]
        
        mapper = {}
        stack = [nums2[0]]
        result = []
        
        for i in range(1, len(nums2)):
            while(stack and nums2[i] > stack[-1]):
                mapper[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for key in stack:
            mapper[key] = -1
        
        for i in nums1:
            result.append(mapper[i])
    
        return result

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    
    output = nextGreaterElement(nums1, nums2)
    print(output)