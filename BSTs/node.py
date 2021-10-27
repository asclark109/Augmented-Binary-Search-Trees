class Node:
    """A class to representing a node. As per CLSR convention, a basic node x has
    
    x.key      satellite data (\"value\")
    x.left     pointer to left child node
    x.right    pointer to right childe node
    x.p        pointer to parent node"""

    def __init__(self, key) -> None:
        
        # initialize parent, left child, right child to null
        self.__p = None
        self.__left = None
        self.__right = None
        self.__key = key
        
    # give decorators to all the instance variables of Node
    @property
    def p(self) -> "Node":
        return self.__p

    @property
    def left(self)-> "Node":
        return self.__left

    @property
    def right(self) -> "Node":
        return self.__right

    @property
    def key(self):
        return self.__key

    # establish setter methods
    @p.setter
    def p(self,new_parent):
        # assert isinstance(new_parent,Node) or issubclass(new_parent,Node) or new_parent is None, "parent object is not a Node object type or subclass of Node"
        self.__p = new_parent

    @left.setter
    def left(self,new_left_child):
        # assert isinstance(new_left_child,Node) or issubclass(new_left_child,Node) or new_left_child is None, "left child object is not a Node object type or subclass of Node"
        self.__left = new_left_child

    @right.setter
    def right(self,new_right_child):
        # assert isinstance(new_right_child,Node) or issubclass(new_right_child,Node) or new_right_child is None, "right child object is not a Node object type or subclass of Node"
        self.__right = new_right_child

    @key.setter
    def key(self,new_key):
        assert isinstance(new_key,self.__key), "new key object is not the same key object type that Node object stores"
        self.__key = new_key

    def __str__(self) -> str:
        return "<{0}>".format(self.key,self.p,self.left,self.right)

    def __repr__(self) -> str:
        return "<key = {0}, parent = {1}, left = {2}, right = {3}>".format(self.key,str(self.p),str(self.left),str(self.right))

    ######### CODE FROM: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def my_display_info(self) -> str:
        return '%s' % self.key

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = self.my_display_info()
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = self.my_display_info()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = self.my_display_info()
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = self.my_display_info()
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        ############################################################################################