class Solution:
    def compress(self, chars: list) -> int:
        if len(chars) < 2:
            return
                
        start = 0
        end = 0

        results = {}

        counter = 1
        for idx, char in enumerate(chars):
            if idx == 0:
                start = idx + 1

            elif char == chars[idx-1]:
                counter += 1
                end = idx + 1
                results[start] = [start, end, counter]

            else:
                start = idx + 1
                counter = 1

        for result in dict(reversed(list(results.items()))).values():
            chars[result[0]:result[1]] = str(result[2])


chars_1 = ["a","a","b","b","c","c","c"]
Solution().compress(chars_1)
print(chars_1)

chars_2 = ["a"]
Solution().compress(chars_2)
print(chars_2)

chars_3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Solution().compress(chars_3)
print(chars_3)