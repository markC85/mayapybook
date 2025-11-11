import sys
import pymel.core as pmc
from pprint import pprint


def syspath():
    """
    Return the current Python system paths as a list of strings
    """
    system_paths = sorted([p.replace("\\", "/") for p in sys.path if p])
    print("sys.paths Found:")
    for path in system_paths:
        print(f'    {path}')


def info(obj):
    """
    Prints information about the object

    Args:
        obj: python object to inspect
    """
    lines = [f'Info for {obj.name()}',
             'Attributes:']
    # Get the name of all attributes
    for a in obj.listAttr():
        lines.append(f'  {a.name()}')

    lines.append(f'MEL type: {obj.type()}')
    lines.append('MRO:')
    lines.extend([' ' + t.__name__ for t in type(obj).__mro__])
    result = '\n'.join(lines)
    print(result)
