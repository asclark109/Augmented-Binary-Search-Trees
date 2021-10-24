# imports
import random

# our imports
from bst import BST
from node import Node
from height_node import HeightNode


# classes
class HeightBST(BST):
    
    def __init__(self, root_node: HeightNode) -> None:
        # ADD assertion that the root node has no parent!
        self.__root = root_node 

    ### instance vars
    @property
    def root(self):
        return self.__root

    ### setter methods
    @root.setter
    def root(self,new_node):
        assert isinstance(new_node,Node) or issubclass(new_node,Node), "new root is not Node type or subclass of Node"
        self.__root = new_node

    def insert(self,z: HeightNode):
        """inserts Node into BST"""

        assert isinstance(z,HeightNode), "HeightNode object to be inserted is not of type HeightNode"

        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        HeightNode.update_heights_upward(z.p)

    def transplant(self, u: Node, v: Node):
        """trasnplants Node z to Node u. Assumes both in Tree"""
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def delete(self,z: Node):
        """Deletes Node from BST. Assumes z in BST!"""

        assert isinstance(z,Node), "node object asked to be deleted is not of type Node"

        if z.left is None:
            self.transplant(z,z.right)
        elif z.right is None:
            self.transplant(z,z.left)
        else:
            y = self.minimum(z.right)
            if y.p is not None:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z,y)
            y.left = z.left
            y.left.p = y


def main():

    # # create a Node
    # node1 = Node(key=20)

    # # create a BST, setting root to be the Node we just made
    # my_tree = BST(node1)

    # # generate and insert 15 random new Nodes into the BST
    # # add 2 specific nodes to test deleting after
    # NUM_NODES = 15
    # for i in range(NUM_NODES):
    #     j = random.randint(1,50)   
    #     my_tree.insert(Node(j))

    # # print BST
    # my_tree.display()
    
    # # print minimum key in BST
    # print("minimum key value: "+str(my_tree.minimum()))

    # # insert 2 nodes. then delete them
    # node_1 = Node(17)
    # node_2 = Node(3)

    # print("inserting 2 nodes:"+str(node_1)+", "+str(node_2))
    # my_tree.insert(node_1)
    # my_tree.insert(node_2)
    # my_tree.display()

    # print("deleting node: "+str(node_1))
    # my_tree.delete(node_1)
    # my_tree.display()
    # print("deleting node: "+str(node_2))
    # my_tree.delete(node_2)
    # my_tree.display()

    # create a Node
    node1 = HeightNode(key=20)

    # create a BST, setting root to be the Node we just made
    my_tree = HeightBST(node1)

    # generate and insert 15 random new Nodes into the BST
    # add 2 specific nodes to test deleting after
    NUM_NODES = 15
    for i in range(NUM_NODES):
        j = random.randint(1,50)   
        my_tree.insert(HeightNode(j))

    # print BST
    my_tree.display()
    
    # # print minimum key in BST
    # print("minimum key value: "+str(my_tree.minimum()))

    # # insert 2 nodes. then delete them
    # node_1 = Node(17)
    # node_2 = Node(3)

    # print("inserting 2 nodes:"+str(node_1)+", "+str(node_2))
    # my_tree.insert(node_1)
    # my_tree.insert(node_2)
    # my_tree.display()

    # print("deleting node: "+str(node_1))
    # my_tree.delete(node_1)
    # my_tree.display()
    # print("deleting node: "+str(node_2))
    # my_tree.delete(node_2)
    # my_tree.display()


if __name__ == "__main__":
    main()