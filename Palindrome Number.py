

def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
         return False
        original_num = x
        rever_num = 0
        while x > 0:
            curr_num = x % 10
            rever_num = rever_num * 10 + curr_num
            x = x // 10
        if original_num == rever_num:
            return True
        else:
            return False