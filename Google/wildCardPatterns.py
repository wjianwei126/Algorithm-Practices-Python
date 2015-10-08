class Solution:
    def wildCardPatterns(self, pattern):
        if not pattern: return []
        for ch in pattern:
            if ch not in '01?':
                return []
        return self.helper(pattern)

    def helper(self, pattern):
        if not pattern: return []
        temp = ''
        i = 0
        result = []
        while i < len(pattern):
            if pattern[i] != '?':
                temp += pattern[i]
                i += 1
            else:
                break
        # if no question mark
        if i == len(pattern):
            return [temp]

        remain = self.helper(pattern[i+1:])
        for res in remain:
            result.append(temp + '0' + res)
            result.append(temp + '1' + res)

        return result

solu = Solution()
pattern = '1?001?101'
print solu.wildCardPatterns(pattern)
