"""
>>> python3 entry.py
>>> python3 -m root.entry

root imported (root.__init__.py executed)
node imported (node.__init__.py executed)
leaf imported (leaf.py executed)
root.node.leaf (__name__ parameter of leaf)

>>> python3 python3 root/node/leaf.py
eaf imported
__main__

>>> python3 -m root.node.leaf
root imported
node imported
leaf imported
__main__
"""
from root.node import leaf
# from root import node.leaf (invalid)
import root.node.leaf # ok
