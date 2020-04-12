"""
>>> python3 [-m] entry.py

Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.7/runpy.py", line 183, in _run_module_as_main
    mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
  File "/opt/anaconda3/lib/python3.7/runpy.py", line 109, in _get_module_details
    __import__(pkg_name)
  File "/Users/Qiuminda/Documents/GitHub/python/hierarchy/root/entry.py", line 9, in <module>
    from root.node import leaf
ModuleNotFoundError: No module named 'root'
"""
# from root.node import leaf


"""
>>> python3 entry.py

node imported (node.__init__.py executed)
leaf imported (leaf.py executed)
node.leaf (__name__ parameter of leaf)
"""
from node import leaf
