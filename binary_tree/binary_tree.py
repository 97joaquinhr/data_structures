class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Queue(object):
    def __init__(self):
        self.items =[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self,start):
        if start is None:
            return
        queue=Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue)>0:
            #traversal += str(queue.peek())+"-"
            node = queue.dequeue()
            traversal += str(node.value)+"-"
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self,start):
        if start is None:
            return
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""       
        while len(queue)>0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack)>0:
            traversal += str(stack.pop().value) + "-"
        return traversal

    def size(self,start):
        if start is None:
            return 0
        return 1+ self.size(start.left)+self.size(start.right)

    def height(self,start):
        if start is None:
            return -1
        left_height = self.height(start.left)
        right_height = self.height(start.right)
        return 1+max(left_height,right_height)
# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5    6     7 
#                         \
#                          8

temp = Node(1)

def invert(start):
    if start:
        invert(start.left)
        invert(start.right)
        temp = start.right
        start.right = start.left
        start.left = temp


# Set up tree:
tree = BinaryTree(12)
tree.root.left = Node(3)
tree.root.right = Node(14)
tree.root.left.left = Node(1)
tree.root.left.right = Node(6)
tree.root.right.left = Node(13)
tree.root.right.right = Node(15)
#tree.root.right.right.right = Node(8)

#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
#print(tree.print_tree("postorder"))
#print(tree.print_tree("levelorder"))
print(tree.print_tree("inorder"))
print(tree.height(tree.root))
print(tree.size(tree.root))


# To check that a binary tree is a correct Binary Search Tree,
# just print the binary tree in-order and if it is a strictly ascending
# sequence, then the binary tree is a correct Binary Search Tree