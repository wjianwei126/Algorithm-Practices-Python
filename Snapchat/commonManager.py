class Employee:
    def __init__(self, name):
        self.name = name
        self.subordinates = []

class Solution:
    def findCommonManager(self, root, employee1, employee2):
        if not root: return None
        self.path1 = []
        self.path2 = []
        self.employee1 = employee1
        self.employee2 = employee2
        self.dfs(root, [root])
        i = 0
        while i < len(self.path1) and i < len(self.path2):
            if self.path1[i] != self.path2[i]:
                break
            i += 1
        return self.path1[i-1].name

    def dfs(self, node, path):
        if node == self.employee1:
            self.path1 = path
            return
        if node == self.employee2:
            self.path2 = path
            return
        for person in node.subordinates:
            self.dfs(person, path + [person])

A = Employee('a')
B = Employee('b')
C = Employee('c')
D = Employee('d')
E = Employee('e')
F = Employee('f')
G = Employee('g')
H = Employee('h')
I = Employee('i')
J = Employee('j')
A.subordinates = [B, C, D]
B.subordinates = [E, F]
C.subordinates = [G]
D.subordinates = [H]
H.subordinates = [I, J]
solution = Solution()
print solution.findCommonManager(A, D, J)
