# License: MIT
# Python: 3.11.6
# Encoding: utf-8
# Date: 2024-01-17
# Author: @neorefraction

# Modules import
import math
import unittest  # Builtin test runner
from src.simple_node import DoubleNode

class TestDoubleNode(unittest.TestCase):
    '''
    A node test class useful to check the correct performance of the node class
    '''

    def test_node_creation(self) -> None:
        '''
        Checks that nodes are created correctly

        TODO: Complete docstrings
        '''

        # 1. Checks if an empty node is correctly created

        # Creates a new empty node
        node1 = DoubleNode()

        # Gets node attributes
        node1_value = node1.get_value()
        node1_parent = node1.get_parent()

        # Checks that node attributes are correct
        self.assertEqual(node1_value, None, f'Invalid value: node1.value = {node1_value} instead of {None}')
        self.assertEqual(node1_parent, None, f'Invalid parent: node1.parent = {node1_parent} instead of {None}')


        # 2. Checks if a node with values is correctly created

        value = 'A'  # Defines a value for the node

        # Creates a new node with a value and node1 as parent
        node2 = DoubleNode(value, node1)

        # Gets node attributes
        node2_value = node2.get_value()
        node2_parent = node2.get_parent()

        # Checks that node attributes are correct
        self.assertEqual(node2_value, value, f'Invalid value: node2.value = {node2_value} instead of {value}')
        self.assertEqual(id(node2_parent), id(node1), f'Invalid parent: node2.parent = {id(node2_parent)} instead of {id(node1)}')

    
    def test_node_update_value(self) -> None:
        '''
        Checks that the value of a node is valid after being modified
        '''

        value = 'A'  # Defines a value for the node
        node = DoubleNode(value) # Creates a new node

        # Changes the node value
        node.set_value(math.pi)

        node_value = node.get_value()

        # Check if the node value has been modified propertly
        self.assertEqual(node_value,  math.pi, f'Invalid node value: node.value = {node_value} instead of {math.pi}')


    def test_node_update_parent(self) -> None:
        '''
        Checks that the parent of a node is valid after being modified
        '''

        # Creates the first node
        node1 = DoubleNode('A')

        # Creates the second node with the first as parent
        node2 = DoubleNode('B') # Creates a new node

        # Sets the node parent
        node2.set_parent(node1)

        node2_parent = node2.get_parent()

        # Check if the node value has been modified propertly
        self.assertEqual(id(node2_parent), id(node1), f'Incorrect node1 parent: node1.parent = {id(node2_parent)} instead of {id(node1)}')
