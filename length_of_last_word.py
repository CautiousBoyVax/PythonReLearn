s = "abcd ab"

def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        "loop from the end, check until the character is not a space"


        end = 0
        if len(s) > 1:
            end = len(s) -1
        else:
             return 1
        lastWordCharCount =0
        foundWord = False
        while not foundWord:
            if s[end] != ' ':
                lastWordCharCount +=1
            
            if s[end] == ' ' and lastWordCharCount > 0:
                foundWord = True
            end -= 1
            if lastWordCharCount == len(s):
                foundWord = True
        return lastWordCharCount

print(lengthOfLastWord(s))