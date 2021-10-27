# imports
import random

# our imports
from bst import BST
from node import Node
from height_node import HeightNode

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

    def delete(self,z: HeightNode):
        """Deletes Node from BST. Assumes z in BST!"""

        assert isinstance(z,HeightNode), "node object asked to be deleted is not of type Node"

        z_parent = z.p                               # new
        if z.left is None:
            self.transplant(z,z.right)
            z_parent.update_heights_upward()         # new
        elif z.right is None:
            self.transplant(z,z.left)
            z_parent.update_heights_upward()         # new
        else:
            y = self.minimum(z.right)
            if y.p is not None:
                self.transplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z,y)
            y.left = z.left
            y.left.p = y
            y.update_heights_upward()         # new


def main():

    # create a Node
    node1 = HeightNode(key=20)

    # create a BST, setting root to be the Node we just made
    my_tree = HeightBST(node1)

    # generate and insert 6 random new Nodes into the BST
    NUM_NODES = 6
    for i in range(NUM_NODES):
        j = random.randint(1,50)   
        my_tree.insert(HeightNode(j))

    # add 2 specific nodes to test deleting after
    # hold onto a reference for them
    node_1 = HeightNode(17)
    node_2 = HeightNode(3)
    print("inserting 2 nodes:"+str(node_1)+", "+str(node_2))
    my_tree.insert(node_1)
    my_tree.insert(node_2)

    # add some more nodes
    NUM_NODES = 6
    for i in range(NUM_NODES):
        j = random.randint(1,50)   
        my_tree.insert(HeightNode(j))

    # print BST
    my_tree.display()
    
    # print minimum key in BST
    print("minimum key value: "+str(my_tree.minimum()))

    # delete nodes
    print("deleting node: "+str(node_1))
    my_tree.delete(node_1)
    my_tree.display()
    print("deleting node: "+str(node_2))
    my_tree.delete(node_2)
    my_tree.display()


if __name__ == "__main__":
    main()