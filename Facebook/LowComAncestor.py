# lowest common ancestor
def lca(node, n1, n2):
  if match(node.left, n1) and match(node.left, n2):
    return lca(node.left, n1, n2) # until we find the least common ancestor by node.left
  if match(node.right, n1) and match(node.right, n2):
    return lca(node.right, n1, n2) # until we find the least common ancestor by node.right
  return node
  
def match(node, n):
  if node is None: return False
  if node == n: return True
  return match(node.left, n) or match(node.rigth, n)