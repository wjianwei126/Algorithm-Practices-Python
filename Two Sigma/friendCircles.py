class Solution:
    def friendCircles(self, friends):
        if not friends or not friends[0]: return 0
        people = set(range(len(friends)))

        friendDic = {}
        for i in xrange(len(friends)):
            connects = set()
            for j in xrange(len(friends[i])):
                if friends[i][j] == 'Y':
                    connects.add(j)
            friendDic[i] = connects
        print friendDic

        circles = []
        for i in xrange(len(friends)):
            if i in people:
                people.remove(i)
                circle = [i]
                connect = friendDic[i]
                while connect:
                    aFriend = connect.pop()
                    if aFriend in people:
                        people.remove(aFriend)
                        connect = connect.union(friendDic[aFriend])
                        circle.append(aFriend)
                circles.append(circle)
        print circles
        return len(circles)

if __name__ == '__main__':
    solu = Solution()
    friends = ['YXYYX', 'XYYXX', 'YYYXX', 'YXXYX', 'XXXXY']
    print solu.friendCircles(friends)
