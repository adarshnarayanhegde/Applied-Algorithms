class Node:
    def __init__(self,key=None):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None


class BinarySearchTree:
    def __init__(self):
        self.root=None

    def tree_insert(self,key):
        z=Node(key)
        y=None
        x=self.root

        while x!=None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.parent=y

        if y==None:
            self.root=z
        elif z.key<y.key:
            y.left=z
        else:
            y.right=z

    traversal=[]
    def _inorder_tree_walk(self,node):
        if node:
            self._inorder_tree_walk(node.left)
            print(node.key)
            self.traversal.append(node.key)
            self._inorder_tree_walk(node.right)
        return self.traversal

    def inorder_tree_walk(self):
        trav=self._inorder_tree_walk(self.root)
        return trav


    count=0
    def _tree_size(self,node):
        if node:
            self._tree_size(node.left)
            self.count+=1
            self._tree_size(node.right)
        return self.count

    def tree_size(self):
        size=self._tree_size(self.root)
        return size


    def _tree_contains(self,node,key):
        if node is None or key==node.key:
            return node
        if key<node.key:
            return self._tree_contains(node.left,key)
        else:
            return self._tree_contains(node.right,key)

    def tree_contains(self,key):
        contain=self._tree_contains(self.root,key)
        if contain:
            return True
        else:
            return False


    def _tree_smallest(self,node):
        x=node
        while x.left!=None:
            x=x.left
        return x

    def tree_smallest(self):
        if self.root:
            smallest=self._tree_smallest(self.root)
            return smallest.key
        else:
            print("Tree Empty")
            exit(0)


    def _tree_largest(self,node):
        x=node
        while x.right!=None:
            x=x.right
        return x

    def tree_largest(self):
        if self.root:
            largest=self._tree_largest(self.root)
            return largest.key
        else:
            print("Tree Empty")
            exit(0)


    def tree_successor(self,key):
        x=self._tree_contains(self.root,key)
        if(x):
            if x.right!=None:
                v=self._tree_smallest(x.right)
                return v.key
            y=x.parent
            while y!=None and x==y.right:
                x=y
                y=y.parent
            if(y):
                return y.key
            else:
                print("%d has no successor!"%(key))
        else:
            print("%d not present in the tree!"%(key))


    def tree_predecessor(self,key):
        x=self._tree_contains(self.root,key)
        if(x):
            if x.left!=None:
                v=self._tree_largest(x.left)
                return v.key
            y=x.parent
            while y!=None and x==y.left:
                x=y
                y=y.parent
            if(y):
                return y.key
            else:
                print("%d has no predecessor!"%(key))
        else:
            print("%d not present in the tree!"%(key))


    sum1=0
    def _greaterSumTree(self,node):
        if node is None:
            return
        self._greaterSumTree(node.right)
        tmp=node.key
        node.key=self.sum1
        self.sum1=node.key+tmp
        self._greaterSumTree(node.left)

    def greaterSumTree(self):
        self._greaterSumTree(self.root)


#Creating a BST
bst=BinarySearchTree()

#Incerting keys into the tree
bst.tree_insert(7)
bst.tree_insert(4)
bst.tree_insert(6)
bst.tree_insert(2)
bst.tree_insert(1)
bst.tree_insert(3)
bst.tree_insert(12)
bst.tree_insert(8)
bst.tree_insert(15)


print("Inorder Traversal of the BST:")
# inorder(): prints elements of the tree inorder
bst.inorder_tree_walk()

print("\n")
# contains(): returns True if key is in the tree, otherwise False
print("Result from contains():",bst.tree_contains(3))

# smallest(): returns the smallest element in the tree
print("Result from smallest():",bst.tree_smallest())

# largest(): returns the largest element in the tree
print("Result from largest():",bst.tree_largest())

# successor(key): returns the smallest element in the tree whose value is greater than key
print("Result from successor():",bst.tree_successor(6))

# predecessor(): returns the largest element in the tree whose value is less than key
print("Result from predecessor():",bst.tree_predecessor(6))

# size(): returns the number of nodes in the tree
print("Result from size():",bst.tree_size())

print("\n")
print("Inorder Traversal Before Converting to GreaterSumTree:")
bst.inorder_tree_walk()

#greaterSumTree(): transforms a given tree so that each node contains the sum of all other keys in the tree which are greater than this node
bst.greaterSumTree()

print("Inorder Traversal After Converting to GreaterSumTree:")
bst.inorder_tree_walk()
