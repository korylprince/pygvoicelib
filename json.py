import simplejson

"""
This is a wrapper around simplejson library to give python 2.4 JSON standard capabilities.
To be compatible with python 2.6 standard JSON library, only loads and dumps must be used.

Notes: Compatible with pythons 2.5+, the exception returned will be a ValueError
"""

__all__ = ['loads', 'dumps']

def convert2str(item):
    """
    This is an implementation to fix a bug with __repr__ function implemenation in python.
    """
    if type(item) is unicode:
        try:
            return str(item)
        except:
            return item
    elif type(item) is list:
        ret = []
        for i in item:
            ret.append(convert2str(i))
        return ret
    elif type(item) is tuple:
        return tuple(convert2str(list(item)))
    elif type(item) is dict:
        ret = {}
        for i in item.keys():
            ret[convert2str(i)] = convert2str(item[i])
        return ret
    else:
        return item

def loads(s):
    intype = type(s)
    try:
        ret = simplejson.loads(s)
    except simplejson.JSONDecodeError:
        raise ValueError(s)
    if intype is str:
        return convert2str(ret)
    else:
        return ret

def dumps(s):
    return simplejson.dumps(s)
