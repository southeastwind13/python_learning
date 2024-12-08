def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """

        mark = []
        
        for i, alphabet in enumerate(s):

            if i == 0:
                print(f"append: {alphabet}")
                mark.append(alphabet)
                pass
            elif alphabet not in mark:
                print(f"append: {alphabet}")
                mark.append(alphabet)
            else:
                print(f"breaking: {alphabet}")
                break
            
        return len(mark)

a = lengthOfLongestSubstring(s="abcabcbb")
print(a)