class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs: return []
        dic = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in dic:
                dic[sortedS].append(s)
            else:
                dic[sortedS] = [s]
        res = []
        for ana in dic.values():
            ana.sort()
            res.append(ana)
        return res

if __name__ == '__main__':
    solu = Solution()
    strs = ['']
    print solu.groupAnagrams(strs)
