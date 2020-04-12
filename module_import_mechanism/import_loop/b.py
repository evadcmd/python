"""
>>> python3 b.py

File "b.py", line 1, in <module>
    from a import a_func
File "/**/a.py", line 22, in <module>
    from b import b_func
File "/**/b.py", line 1, in <module>
    from a import a_func
ImportError: cannot import name 'a_func' from 'a' 

"""
from a import a_func

def b_func():
    pass