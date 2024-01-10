#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        
        # Recursive call to find the kth symbol in the previous row (n-1)
        prev_k = (k + 1) // 2  # Calculate the corresponding position in the previous row
        
        # Recursive call to find the symbol in the previous row (n-1)
        prev_symbol = self.kthGrammar(n - 1, prev_k)
        
        # If the symbol in the previous row is 0, the pattern is 01, else it's 10
        if prev_symbol == 0:
            if k % 2 == 1:
                return 0
            else:
                return 1
        else:
            if k % 2 == 1:
                return 1
            else:
                return 0


# In[4]:


n=5
k=3
solution = Solution()
result = solution.kthGrammar(n,k)


# In[5]:


result


# In[ ]:




