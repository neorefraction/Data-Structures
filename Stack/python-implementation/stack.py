from node import Node

class Stack:
    '''
    Stack class implements the stack data structure using nodes with references 
    instead of the python built-in list class

    Attributes:
        __top: reference to the top of the stack
        __lenght: integers that watchs the length of the stack
    '''

    def __init__(self, top: 'Node' = None):
        '''
        Constructs a new stack empty or with a initial node

        Args:
            lenght: Lenght of the stack
        '''
        self.__top = top

        self.__lenght = 0

        if top.get_parent():
            node = top
            while node.get_parent():
                self.__lenght += 1
                node = node.get_parent()

    def copy(self) -> 'Node':
        '''
        Returns a copy of the stack

        Returns:
            a copy of the whole stack
        '''

        # Step 1: Make a copy of the top
        top = Node(self.top().get_object(), self.top().get_parent())

        # Step 3: Make copies of each node
        node = top  # Initialize a centinel node with the top

        # Loops througth the whole stack
        while node.get_parent():

            # Gets the parent of the sentinel
            parent = node.get_parent()

            # Sets the parent to a copy of it
            node.set_parent(Node(parent.get_object(), parent.get_parent()))

            # Updates the sentinel node
            node = parent
        
        return Stack(top)

    
    def add_node(self, node: 'Node') -> None:
        '''
        Adds a node to the stack

        Args:
            node: The node to be added
        '''

        # It has no sense to a None node
        if not node:
            raise TypeError('Null node is not valid')
        
        # Step 1: Set the top of the stack as the parent of the new node
        node.set_parent(self.__top)

        # Step 2: Set the new node as the new top of the stack
        self.__top = node

        # Step 3: Increment the lenght of the stack
        self.__lenght += 1
    
    def pop(self) -> 'Node':
        '''
        Removes the top element of the stack

        Returns:
            The removed element
        '''

        # Step 1: Save the top element
        node = self.__top

        # Step 2: Set the parent of the top as the new top
        self.__top = self.__top.get_parent()

        # Step 3: Return the saved element
        return node

    def top(self) -> 'Node':
        '''
        Returns the top node

        Returns:
            a reference of the top node
        '''

        return self.__top
        

    def size(self) -> int:
        '''
        Returs the size of the stack

        Returs:
            integer with the size of the stack
        '''

        return self.__lenght
    
    def empty(self) -> bool:
        '''
        Returns true if the stack is empty

        Returns:
            true if is empty, false otherwise
        ''' 

        return self.__lenght == 0
    
    def __repr__(self) -> str:
        output = '['

        node = self.__top

        while node:
            output += str(node) + ', '
            node = node.get_parent()
        
        return output + ']'


if __name__ == '__main__':

    # Creates an empty stack
    stack = Stack()

    # Add some values to the stack
    for i in range(3):
        stack.add_node(Node(i))
    
    print(f'Stack before pop: {stack}')
    print(f'Pop value: {stack.pop()}')
    print(f'Stack after pop: {stack}')

    # Creates an empty stack to copy the first one
    copied_stack = Stack()

    copied_stack.copy()
