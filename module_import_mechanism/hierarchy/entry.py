"""
>>> python3 entry.py

root imported (root.__init__.py executed)
node imported (node.__init__.py executed)
leaf imported (leaf.py executed)
root.node.leaf (__name__ parameter of leaf)
"""
from root.node import leaf
