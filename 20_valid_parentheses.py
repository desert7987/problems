class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        open_ = {'(', '{', '['}
        close_ = {'(': ')', '{': '}', '[': ']'}

        open_brackets = []
        for bracket in s:
            if bracket in open_:
                open_brackets.append(bracket)
            else:
                if not open_brackets:
                    return False
                x = open_brackets.pop()
                if bracket != close_[x]:
                    return False
        if open_brackets:
            return False
            
        return True