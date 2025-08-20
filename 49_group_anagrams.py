from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        if not strs:
            return [[""]]

        if len(strs) == 1:
            return [strs]

        data = defaultdict(list)

        for text in strs:
            key = str(sorted(text))
            data[key].append(text)

        return list(data.values())