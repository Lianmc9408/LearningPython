class TreeNode():
    def __init__(self, data=0, left=0, right=0):
        self.data = data
        self.left = left
        self.right = right


class Tree():
    def __init__(self, root):
        self.root = root

    def preOrder(self, treenode):
        if treenode is 0:
            return
        print(treenode.data)
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)

    def inOrder(self, treenode):
        if treenode is 0:
            return
        self.inOrder(treenode.left)
        print(treenode.data)
        self.inOrder(treenode.right)

    def postOrder(self, treenode):
        if treenode is 0:
            return
        self.postOrder(treenode.left)
        self.postOrder(treenode.right)
        print(treenode.data)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2, n1, 0)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n3, n4)
    n6 = TreeNode(6, n2, n5)
    n7 = TreeNode(7, n6, 0)
    n8 = TreeNode(8)
    root = TreeNode('root', n7, n8)

    tree = Tree(root)
    print('preOrder'.center(50, '-'))
    tree.preOrder(tree.root)

    print('inOrder'.center(50, '-'))
    tree.inOrder(tree.root)

    print('postOrder'.center(50, '-'))
    tree.postOrder(tree.root)
