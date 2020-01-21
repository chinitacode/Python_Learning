import re

p = re.compile('[a-z]+')
p_non_greedy = re.compile('[a-z]+?')

if __name__ == '__main__':
    print(p.match("")) # None, since + means ‘one or more repetitions’
    print(p.match('tempo'))  # <re.Match object; span=(0, 5), match='tempo'>
    print(p_non_greedy.match('tempo')) # <re.Match object; span=(0, 1), match='t'>


'''
can query the match object for information about the matching string.
Match object instances also have several methods and attributes;
the most important ones are:

Method/Attribute                             Purpose

group()                      Return the string matched by the RE

start()                      Return the starting position of the match

end()                        Return the ending position of the match

span()                       Return a tuple containing the (start, end) positions of the match

>>> m
<re.Match object; span=(0, 5), match='tempo'>

>>> m.group()
'tempo'
>>> m.start()
0
>>> m.end()
5
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)


group() returns the substring that was matched by the RE.
start() and end() return the starting and ending index of the match.
span() returns both start and end indexes in a single tuple.
Since the match() method only checks if the RE matches at the start of a string,
start() will always be zero.
However, the search() method of patterns scans through the string,
so the match may not start at zero in that case.

>>> print(p.match('::: message'))
None
>>> m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
>>> m.group()
'message'
>>> m.span()
(4, 11)


In actual programs, the most common style is to store the match object in a variable,
and then check if it was None. This usually looks like:

p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')


'''
