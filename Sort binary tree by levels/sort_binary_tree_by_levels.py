'''Sort binary tree by levels'''
from collections import deque
class Node:
    '''Node'''
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
    def __str__(self) -> str:
        return f"Node({self.value})"
    def __repr__(self) -> str:
        return f"Node({self.value})"

def tree_by_levels(node):
    '''Sort binary tree by levels'''
    output = []
    q = deque()
    if node:
        q.append(node)
    while q:
        curr = q.pop()
        output.append(curr.value)
        if curr.left:
            q.appendleft(curr.left)
        if curr.right:
            q.appendleft(curr.right)
    return output

if __name__=='__main__':
    tree = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
    print(tree_by_levels(tree))