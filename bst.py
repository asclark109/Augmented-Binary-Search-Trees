# imports
import random

# our imports
from node import Node


# classes
class BST:
    
    def __init__(self, root_node: Node) -> None:
        # ADD assertion that the root node has no parent!
        self.__root = root_node    

    ### instance vars
    @property
    def root(self):
        return self.__root

    ### setter methods
    @root.setter
    def root(self,new_node):
        assert isinstance(new_node,self.__key), "new root is not Node type"
        self.__root = new_node

    ### instance methods
    def display(self):
        return self.root.display()

    def insert(self,z: Node):
        assert isinstance(z,Node), "node object provided is not of type Node"

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



def main():

    # create a Node
    node1 = Node(key=20)

    # create a BST, setting root to be the Node we just made
    my_tree = BST(node1)

    # generate and insert 15 random new Nodes into the BST
    NUM_NODES = 15
    for i in range(NUM_NODES):
        j = random.randint(1,50)   
        my_tree.insert(Node(j))

    # print BST
    my_tree.display()


if __name__ == "__main__":
    main()