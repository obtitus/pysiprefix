from __future__ import division
import math

unit = {9: 'G', 6: 'M', 3: 'k', 0: '',        
        -3: 'm', -6: '\\textmu ', -9: 'n', -12: 'p', -15: 'f', -18: 'a', -21: 'z'}

def e(n):
    '''Takes a float n and returns scaled version (float) and scaling (str)'''
    scale, unit = engineeringUnit(n)
    return n/10**scale, unit

def engineeringUnit(n):
    '''Takes a float n and returns the scaling (integer) and scaling (str)'''
    try:
        x = int(math.log10(abs(n))//3)*3
    except ValueError:
        x = 0
    except TypeError:
        return n, ''
    try:
        u = unit[x]
    except KeyError:
        x = 0
    return x, unit[x]

def scale(u):
    '''Takes a string u and returns scaling'''
    for key in unit:
        if unit[key].lower() == u.lower():
            return 10**key
    else:
        raise KeyError('Could not find value {}'.format(u))
# print engineeringUnit(10)
# print engineeringUnit(100)
# print engineeringUnit(1000)
# print engineeringUnit(1e-3)
