import heapq
class TreeNode(object):
    def __init__(self, freq, val='#'):
        self.left = None
        self.right = None
        self.freq = freq
        self.val = val

def huffmanCoding(dataFreq):
    minHeap = []
    root = buildTree(dataFreq)
    res = {}
    encode(root, '', res)
    print res

def buildTree(dataFreq):
    minHeap = []
    for key in dataFreq:
        leaf = TreeNode(dataFreq[key], key)
        heapq.heappush(minHeap, (dataFreq[key], leaf))

    while len(minHeap) > 1:
        leftChild = heapq.heappop(minHeap)[1]
        rightChild = heapq.heappop(minHeap)[1]
        internalNode = TreeNode(leftChild.freq + rightChild.freq)
        internalNode.left = leftChild
        internalNode.right = rightChild
        heapq.heappush(minHeap, (leftChild.freq + rightChild.freq, internalNode))

    return heapq.heappop(minHeap)[1]

def encode(node, path, dic):
    if node.left:
        encode(node.left, path+'0', dic)
    if node.right:
        encode(node.right, path+'1', dic)
    if not node.left and not node.right:
        dic[node.val] = path

dataFreq = {'a':5, 'b':9, 'c':12, 'd':13, 'e':16, 'f':45}
huffmanCoding(dataFreq)
