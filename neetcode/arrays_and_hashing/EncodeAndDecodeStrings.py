class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        result = ""
        for string in strs:
            result += str(len(string)) + "/" + string
        return result

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        result = []
        pointer = 0
        while pointer < len(str):
            i = pointer
            while str[i] != "/":
                i += 1
            length = len(str[pointer : i])
            result.append(str[i + 1 : i + 1 + length])
            pointer = i + 1 + length
        return result
