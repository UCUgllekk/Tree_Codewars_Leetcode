'''Tree Traversal'''
class Node:
    '''Node'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"Node(data={self.data}, left = {self.left}, right = {self.right})"

    def __repr__(self) -> str:
        return f"Node(data={self.data})"


def pre_order(node):
    '''Travel throught tree in pre-order'''
    # output = []
    # stk = []
    # curr = node
    # while True:
    #     if curr is not None:
    #         stk.append(curr)
    #         output.append(curr.data)
    #         curr = curr.left
    #     else:
    #         if not stk:
    #             break
    #         curr = stk.pop().right
    # return output
    if node is None:
        return []
    left = pre_order(node.left)
    right = pre_order(node.right)
    return [node.data] + left + right

def in_order(node):
    '''Travel throught tree in in-order'''
    # output = []
    # stk = []
    # curr = node
    # while True:
    #     if curr is not None:
    #         stk.append(curr)
    #         curr = curr.left
    #     else:
    #         if not stk:
    #             break
    #         output.append(stk[-1].data)
    #         curr = stk.pop().right
    # return output

    if node is None:
        return []
    left = in_order(node.left)
    right = in_order(node.right)
    return left + [node.data] + right

def post_order(node):
    '''Travel throught tree in post-order'''
    if node is None:
        return []
    left = post_order(node.left)
    right = post_order(node.right)
    return left + right + [node.data]

def test():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    a.left = b
    a.right = c
    c.left = d
    assert pre_order(a) == ['A', 'B', 'C', 'D'], pre_order(a)
    assert in_order(a) == ['B', 'A', 'D', 'C'], in_order(a)
    assert post_order(a) == ["B", "D", "C", "A"], post_order(a)

if __name__=="__main__":
    test()
