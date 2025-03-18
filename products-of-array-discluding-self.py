                prod[i] = prod[i-1] * nums[i]
        
        for i in range(len(nums)-1,-1, -1):
            if i == len(nums)-1:
                rev_prod[i] = nums[i]
            else:
                rev_prod[i] = rev_prod[i+1]*nums[i]
        
        for i in range(len(nums)):
            if i == 0:
