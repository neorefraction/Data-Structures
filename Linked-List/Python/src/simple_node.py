# License: MIT
# Python: 3.11.6
# Encoding: utf-8
# Date: 2024-01-17
# Author: @neorefraction

from typing import Any

class DoubleNode:
    '''
    TODO: Complete docstirngs

    Attributes:
        value:
        parent: 
    '''
    
    def __init__(self, value: Any = None, parent: 'DoubleNode' = None):
        self.set_value(value)
        self.set_parent(parent)

    def set_value(self, value: Any):
        '''
        TODO: Complete docstrings
        '''

        self.value = value

    def get_value(self) -> Any:
        '''
        TODO: Complete docstrings
        '''

        return self.value

    def set_parent(self, parent: 'DoubleNode'):
        '''
        TODO: Complete docstrings
        '''

        if parent is not None and not isinstance(parent, DoubleNode):
            raise TypeError('Node parent must be a DoubleNode object')

        self.parent = parent

    def get_parent(self) -> 'DoubleNode':
        '''
        TODO: Complete docstrings
        '''

        return self.parent
    