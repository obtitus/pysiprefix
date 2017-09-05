from __future__ import division

try:
    import numpy as np
except ImportError as e:
    print('Warning, numpy not found, no support for complex numbers %s', e)

import eUnit

def n(num, sig=3, latexE=True):
  format = '%.' + str(sig) + 'g'
  ret = format % num
  if latexE and 'e' in ret:
      ret = ret.replace('e', r'\e{')
      ret += '}'
  return ret
approx = n

def SI(num, unit='', sig=3, autoScale=True, complex=False):
    """Takes a number 'num' and returns \SI{num}{unit}, if 'autoScale' is true, the unit
    is pre-pended with a si-prefix (kilo, mega, micro...)."""
    if unit == '':
        autoScale = False

    if autoScale:
        num, siPrefix = eUnit.e(num)
        siPrefix = siPrefix.replace('$', '')
    else:
        siPrefix = ''
    unit = unit.replace(';', '\\')
    if complex:
        num_float_re = np.real(num)
        num_float_im = np.imag(num)
        num_re = approx(num_float_re, sig=sig, latexE=False)
        num_im = approx(num_float_im, sig=sig, latexE=False)
        num = ''
        if num_re != '0':
            num = num_re + ' '

        if '-' in num_im: #num_float_im > 0
            num += "- j" + num_im.replace('-', '')
        elif num_im == '0':
            pass
        else:
            num += '+ j' + num_im
    else:
        num = approx(num, sig=sig, latexE=False)
    res = r'\SI{%s}{%s{}%s}' % (num, siPrefix, unit)
    res = res.strip()
    res = res.replace('nan', '')
    res = res.replace(r'\textmu', r'\micro')  
    
    #logger.debug('SI: %s', res)
    return res


def v(name, value, unit='', dollar=True, approx=False, **kwargs):
    r"""takes a 'name' and 'value' and returns '$name = \SI{value}{unit}$', extra arguments sent to SI.
    Set dollar to False to suppress the enclosing '$' signs.
    >>> v('f_o', 1e9, 'Hz')
    '$f_o = \\SI{1}{G{}Hz}$'
    """
    if dollar:
        fmt = '${0} = {1}$'
    else:
        fmt = '{0} = {1}'
    if approx:
        fmt = fmt.replace('=', r'\approx')
    return fmt.format(name, SI(value, unit, **kwargs))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
