# 输入一句以及一个阀值k，要求把这句话 分割 成 List<String>。要求List中的每个String满足以下条件：
# 1.长度<=k且尽量接近K
# 2.不能以空格开头或结尾，但是中间可以有空格.1point3acres缃�
# 3.不能从单词中间切开
# 4.特殊情况下允许String长度>k：句子中有长度>k的单词。
# 比如
# 输入 “abcd e fg hijklmn o p q r”, k=5
# 输出 ["abcd", "e fg", "hijklmn", "o p q", "r"]
class Solution:
    def textJustification(self, s, k):
        if not s: return ['']
        stringList = s.split(' ')
        res = []
        i = 0
        temp = ''
        while i < len(stringList):
            if len(stringList[i]) >= k:
                if len(temp) > 0:
                    res.append(temp)
                    temp = ''
                res.append(stringList[i])
                i += 1
                continue
            if len(temp) == 0:
                temp = stringList[i]
            elif len(temp + ' ' + stringList[i]) > k:
                res.append(temp)
                temp = stringList[i]
            else:
                temp += ' ' + stringList[i]
            i += 1

        if len(temp) > 0:
            res.append(temp)

        return res

solution = Solution()
s = 'abcd e fg hijklmn o p q r'
print solution.textJustification(s, 5)
