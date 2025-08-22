class Solution:
    def maxPower(self, s: str) -> int:
        last = ''
        count = 1
        data = {'max': 1}
        for character in s:
            if character == last:
                count += 1
                if data['max'] < count:
                    data['max'] = count
            else:
                count = 1
                last = character
        return data['max']