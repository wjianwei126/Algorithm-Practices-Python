class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.possibleRoots = set()
        self.nodes = {}

    def insertEdge(self, parent, child):
        if not self.root:
            parentNode = TreeNode(parent)
            childNode = TreeNode(child)
            self.possibleRoots.add(parentNode)
            parentNode.children.append(childNode)
            self.nodes[parent] = parentNode
            self.nodes[child] = childNode
        else:
            if parent in self.nodes and child in self.nodes:
                self.nodes[parent].children.append(self.nodes[child])
                if self.nodes[child] in self.possibleRoots:
                    self.possibleRoots.remove(self.nodes[child])
            elif parent in self.nodes and child not in self.nodes:
                childNode = TreeNode(child)
                self.nodes[child] = childNode
                self.nodes[parent].children.append(childNode)
            elif parent not in self.nodes and child in self.nodes:
                parentNode = TreeNode(parent)
                self.nodes[parent] = parentNode
                self.nodes[parent].children.apped(self.nodes[child])
                if self.nodes[child] in self.possibleRoots:
                    self.possibleRoots.remove(self.nodes[child])
                self.possibleRoots.add(self.nodes[parent])
            else:
                parentNode = TreeNode(parent)
                childNode = TreeNode(child)
                self.possibleRoots.add(parentNode)
                parentNode.children.append(childNode)
                self.nodes[parent] = parentNode
                self.nodes[child] = childNode
        if len(self.possibleRoots) == 1:
            self.root = list(self.possibleRoots)[0]

    def preorderTraversal(self):
        node = self.root
        stack = []
        while stack or node:
            if node:
                print node.val
                if len(node.children) > 1:
                    for i in range(1, len(node.children)):
                        stack.append(node.children[i])
                node = node.children[0] if node.children else None
            else:
                node = stack.pop()

    def getLeafMax(self):
        node = self.root
        self.dfs(node, node.val)

    def dfs(self, node, curMax):
        if not node.children:
            print node.val, curMax
            return

        for child in node.children:
            self.dfs(child, max(curMax, child.val))

class SolutionWithoutTreeConstruction:
    def getLeafMax(self, edges):
        if not edges: return
        leaves = set()
        allNodes = set()
        parentMap = {}

        # construct parentMap and leaf set
        # {10: 5, 15: 5, 5: 8, 6: 8, 7: 6}, set([10, 15, 7])
        for parent, child in edges:
            parentMap[child] = parent
            if parent in leaves:
                leaves.remove(parent)
            if child not in allNodes:
                leaves.add(child)
            allNodes.add(parent)
            allNodes.add(child)

        # Search for each leaf in the leaf set
        for leaf in leaves:
            curMax = leaf
            node = leaf
            while node in parentMap:
                node = parentMap[node]
                curMax = max(node, curMax)
            curMax = max(node, curMax)
            print leaf, curMax


tree = Tree()
edges = [(5, 10), (8, 6), (6, 7), (5, 15), (8, 5)]
for edge in edges:
    tree.insertEdge(edge[0], edge[1])
# tree.preorderTraversal()
tree.getLeafMax()
solution = SolutionWithoutTreeConstruction()
solution.getLeafMax(edges)
