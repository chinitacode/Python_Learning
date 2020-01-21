'''
Two pattern methods return all of the matches for a pattern.
findall() returns a list of matching strings:
'''
import re



if __name__ == '__main__':
    # greedy
    p = re.compile(r'\d+')
    print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
    # ['12', '11', '10']

    # non-greedy
    p = re.compile(r'\d+?')
    print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
    # ['1', '2', '1', '1', '1', '0']

'''
The r prefix, making the literal a raw string literal,
is needed in this example because escape sequences in a normal “cooked” string literal
that are not recognized by Python, as opposed to regular expressions,
now result in a DeprecationWarning and will eventually become a SyntaxError.

findall() has to create the entire list before it can be returned as the result.
The finditer() method returns a sequence of match object instances as an iterator:

>>> iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
>>> iterator
<callable_iterator object at 0x...>
>>> for match in iterator:
...     print(match.span())
...
(0, 2)
(22, 24)
(29, 31)
'''
