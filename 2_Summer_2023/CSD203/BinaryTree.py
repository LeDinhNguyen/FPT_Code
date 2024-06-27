class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, node: Node) -> None:
        self.root = node

    def height(self, node: Node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
    
    def nodeLevel(self, node: Node, level: int):
        if node is None:
            return 0
        elif level == 1:
            print(node.data, end=" ")
        else:
            self.nodeLevel(node.left, level - 1)
            self.nodeLevel(node.right, level - 1)
    
    def levelOrder(self, node: Node):
        height = self.height(node)
        for i in range(height):
            self.nodeLevel(node, i + 1)
            print()


    def inOrder(self, node: Node):
        if node:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.right)


    def preOrder(self, node: Node):
        if node:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def postOrder(self, node: Node):
        if node:
            self.postOrder(node.right)
            self.postOrder(node.left)
            print(node.data, end=" ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    b = BinaryTree(root)
    print("Inorder Traversal:", end=" ")
    b.inOrder(root)
    print()
    print("Preorder Traversal:", end=" ")
    b.preOrder(root)
    print()
    print("Postorder Traversal:", end=" ")
    b.postOrder(root)
    print()
    b.levelOrder(root)