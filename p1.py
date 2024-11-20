# test

class Solution:
    def myAtoi(self, s: str) -> int:
        resultStr = []
        idx = 0

        # skip leading whitespaces
        while idx < len(s) and s[idx] == " ":
            idx += 1
        
        # handle signs
        if idx < len(s) and (s[idx] == "+" or s[idx] == "-"):
            resultStr.append(s[idx])
            idx += 1
        
        # process digits
        while idx < len(s)and s[idx].isdigit():
            resultStr.append(s[idx])
            idx += 1
        
        # convert to integer
        if resultStr == [] or (len(resultStr)) == 1 and (resultStr[0] == "+" or resultStr[0] == "-"):
            return 0

        resultInt = int("".join(resultStr))

        # clamp result within 32-bit integer bound
        if resultInt < -(2**31):
            resultInt = -(2**31)
        elif resultInt > (2**31 - 1):
            resultInt = 2**31 - 1
        
        return resultInt