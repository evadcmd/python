"""
>>> python3 a.py

Traceback (most recent call last):
  File "A.py", line 1, in <module>
    from B import b_func # 
  File "/**/B.py", line 1, in <module>
    from A import a_func # 
  File "/**/A.py", line 1, in <module>
    from B import b_func
ImportError: cannot import name 'b_func' from 'B'

read line1 of a.py 
=> import b => b not in sys.modules => construct empty dict of module b
=> read b.py => read line1 of b.py
=> import a => a not in sys.modules => construct empty dict of module a

=> read line1 of a.py
=> b in sys.modules
=> from module b's dict(empty) read b_func => raise ImportError

"""
from b import b_func

def a_func():
    pass