# Basic Formatting
print('Old style: %s %s' % ('one', 'two'))
print('new style: {} {}'.format('one', 'two'))
print('Old style: %d %d' % (1, 2))
print('new style: {} {}'.format(1, 2))
print('new style: {1} {0} {1}'.format('one', 'two'))  # positional index, not available in old style


# Value Conversion: r: repr(), a: ascii(), s: str()
class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


print('Old style: %s %r' % (Data(), Data()))
print('new style: {0!s} {0!r}'.format(Data()))


class Data2(object):
    def __repr__(self):
        return 'räpr'


print('Old style: %r %a' % (Data2(), Data2()))
print('new style: {0!r} {0!a}'.format(Data2()))


# Padding and aligning strings
# align right
print('Old style: %10s' % ('test',))
print('new style: {:>10}'.format('test'))
# align left
print('Old style: %-10s' % ('test',))
print('new style: {:<10}'.format('test'))
# choose align value
print('new style: {:_<10}'.format('test'))
# align center
print('new style: {:_^10}'.format('test'))
print('new style: {:_^7}'.format('test'))  # right will have one more padding


# Truncating long strings
print('Old style: %.5s___' % ('xylophone',))
print('new style: {:.5}___'.format('xylophone'))


# Combining truncating and padding
print('Old style: %-10.5s___' % ('xylophone',))
print('new style: {:10.5}___'.format('xylophone'))


# refer to the below link for more examples
# https://pyformat.info/
