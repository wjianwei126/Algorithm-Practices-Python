# Design a data structure to store an HTML DOM
# And use it to compare the pure text in two documents, return if it is the same

class DOMNode:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text
        self.children = []

class DOMTree:
    def pureTextIsEqual(self, node1, node2):
        if not node1 and node2: return False
        if not node2 and node2: return False
        text1 = self.getPureText(node1)
        text2 = self.getPureText(node2)
        return text1 == text2

    def getPureText(self, node):
        if not node: return ''
        res = ''
        if node.children:
            for child in node.children:
                res += self.getPureText(child)
        res += node.text
        return res

A = DOMNode('HTML', '')
B = DOMNode('body', '')
C = DOMNode('p', 'Hello')
A.children.append(B)
B.children.append(C)

D = DOMNode('HTML', '')
E = DOMNode('body', '')
F = DOMNode('p', 'llo')
G = DOMNode('b', 'H')
H = DOMNode('span', 'e')
D.children.append(E)
E.children.append(F)
F.children.append(G)
F.children.append(H)

tree = DOMTree()
print tree.pureTextIsEqual(A, D)
