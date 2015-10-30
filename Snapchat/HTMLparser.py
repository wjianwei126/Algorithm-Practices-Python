class DOMNode:
    def __init__(self, tag, content = '', attr = None):
        self.tag = tag
        self.content = content
        self.attr = attr
        self.children = []

    def beginTag(self):
        if not self.attr:
            return '<' + self.tag + '>'
        outputTag = '<' + self.tag
        for attribute in self.attr:
            outputTag += ' ' + attribute + '=' + self.attr[attribute]
        outputTag += '>'
        return outputTag

    def endTag(self):
        return '</' + self.tag + '>'

class HTMLDOM:
    def __init__(self, root):
        self.root = root

    def toString(self):
        self.output = ''
        self.dfs(self.root)
        return self.output

    def dfs(self, node):
        if not node: return
        self.output += node.beginTag() + node.content
        for child in node.children:
            self.dfs(child)
        self.output += node.endTag()

HTML = DOMNode('html')
BODY = DOMNode('body')
STRONG = DOMNode('strong', 'hello')
A = DOMNode('a', 'world', {'html':"http://helloworld.com"})
HTML.children = [BODY]
BODY.children = [STRONG, A]
domTree = HTMLDOM(HTML)
print domTree.toString()
