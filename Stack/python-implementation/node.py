# TODO: Comment correctly the class

class Node:
    '''
    This class is a representation of a stack node.
    It stores an object to make the stack generic and a pointer to the parent node

    Attributes:
        __object: Object with more information stored by the node
        __parent: Pointer to the parent node
    '''

    def __init__(self, object: any = None, parent: 'Node' = None):
        '''
        Constructs a node

        Args:
            object: The object to be stored
            parent: Pointer to the parent node
        '''

        self.__object = object
        self.__parent = parent

    def set_object(self, object: any) -> None:
        '''
        Sets the node stored object

        Args:
            object: The new object to be stored
        
        Raises:
            TypeError: If `object` is None it can't be setted
        '''

        if not object:
            raise ValueError('No object given to store')
        
        self.__object = object  # Sets the stored object

    def get_object(self) -> any:
        '''
        Gets the object stored

        Returns:
            The object of the node
        '''

        return self.__object
    
    def set_parent(self, parent: 'Node') -> None:
        '''
        Sets the parent of the node

        Args:
            parent: Parent node
        '''

        self.__parent = parent  # Sets the parent
    
    def get_parent(self) -> 'Node':
        '''
        Gets the parent of the node

        Returns:
            The parent node 
        '''
        return self.__parent

    def __repr__(self) -> str:
        '''
        Returns a string representation of the node.
        Format -> Node: representation of the object stored
        '''
        return f'Node: {str(self.__object)}'