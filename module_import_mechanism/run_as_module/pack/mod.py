"""
under hierachy2 folder

>>> python3 pack/mod.py

mod imported # pack not imported
__name__: __main__
__package__: None
__file__: 'pack/mod.py' # relative path
modulename: <module '__main__' from 'pack/mod.py'>
sys.path: ['/**/hierarchy2/pack', *other_paths]

>>> python3 -m pack.mod

pack imported # inner_pack not imported
mod imported
__name__: __main__
__package__: pack
__file__: '/**/hierarchy2/pack/mod.py' # abs path
modulename: <module 'pack.mod' from '/**/hierarchy2/pack/mod.py'>
sys.path: ['/**/hierarchy2', *other_paths]
"""

import sys

print('mod imported')
print(f'__name__: {__name__}')
print(f'__package__: {__package__}')
print(f'__file__: {__file__}')
print(f'sys.path: {sys.path}')
print(f'modulename: {sys.modules[__name__]}')