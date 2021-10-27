from node import Node


from node import Node

class HeightNode(Node):
    """A node that contains extra data about its children nodes: the height
    
    inherited from Node class:

    x.key      satellite data (\"value\")
    x.left     pointer to left child node
    x.right    pointer to right childe node
    x.p        pointer to parent node
    
    new instance variables:

    x.height   height of tree made where x is the root"""

    def __init__(self, key) -> None:
        
        # initialize parent, left child, right child to null
        self.__key = key
        self.__height = 0
        self.__p = None
        self.__left = None
        self.__right = None

    @property
    def p(self) -> "HeightNode":
        return self.__p

    @property
    def left(self)-> "HeightNode":
        return self.__left

    @property
    def right(self) -> "HeightNode":
        return self.__right

    @property
    def key(self):
        return self.__key

    @p.setter
    def p(self,new_parent):
        self.__p = new_parent

    @left.setter
    def left(self,new_left_child):
        self.__left = new_left_child

    @right.setter
    def right(self,new_right_child):
        self.__right = new_right_child

    @key.setter
    def key(self,new_key):
        assert isinstance(new_key,self.__key), "new key object is not the same key object type that HeightNode object stores"
        self.__key = new_key

    # new 
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,height):
        assert isinstance(height,int), "height is not an int type."
        self.__height = height

    #new

    def my_display_info(self) -> str:
        return '{0}, ht={1}'.format(self.key,self.height)

    def __str__(self) -> str:
        return "<{0},{1}>".format(self.key,self.height)

    def __repr__(self) -> str:
        return "<key = {0}, parent = {1}, left = {2}, right = {3}, height = {4}>".format(self.key,str(self.p),str(self.left),str(self.right),str(self.height))
    
    def update_heights_upward(x: "HeightNode"):
        """updates height of x and all ancestor nodes"""

        assert isinstance(x,HeightNode) or x is None, "HeightNode object provided is not of type HeightNode (or None)"

        if x is not None: 
            if x.left is None and x.right is None:
                x.height = 0
            elif x.left is None:
                x.height = x.right.height + 1
            elif x.right is None:
                x.height = x.left.height + 1
            else:
                x.height = max(x.left.height+1, x.right.height+1)
            HeightNode.update_heights_upward(x.p)
