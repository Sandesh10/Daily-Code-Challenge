class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluate_tree(root):
    if root is None:
        return 0
    left = evaluate_tree(root.left)
    right = evaluate_tree(root.right)
    return 1+ left +right if is_unival(root, root.value) else left+right

def is_unival(root,value):
    if root is None:
        return True
    if root.value = value:
        return is_unival(root.left, value) and is_unival(root.right, value)
    return False

def main():
    n1 = Node(0)
    n2 = Node(1)
    n3 = Node(0)
    n4 = Node(1)
    n5 = Node(0)
    n6 = Node(1)
    n7 = Node(1)
        
