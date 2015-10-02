# http://www.1point3acres.com/bbs/thread-143180-1-1.html
# Suppose we have the following API available
# isFile(), isDirectory(), getFileOrDirectory()
# input: the original position in the file system, e.g. ~/
# output: None, just print the file system hierarchy under the input path
class Solution:
    def printHierarchyIterative(self, path):
        if not path: return
        stack = [(path, 1)]
        while stack:
            node, indentation = stack.pop()
            print '-' * indentation + node
            if node.isFile():
                continue
            if node.isDirectory():
                for fileOrDir in node.getFileOrDirectory():
                    stack.append((fireOrDic, indentation + 1))

    def printHierarchyRecursive(self, path):
        if not path: return
        self.helper(path, 1)
        return

    def helper(self, node, indentation):
        print '-' * indentation + node
        if node.isDirectory():
            for fileOrDir in node.getFileOrDirectory():
                 self.helper(fileOrDir, indentation + 1)
        return
