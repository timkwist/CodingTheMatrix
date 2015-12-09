# Author: Tim Kwist
# Since this lab is most an introduction to python that demonstrates how to use the language, this session was mostly just playing
# around in the command line. Therefore, the commands from here on out are just a copy/paste of what I did in the terminal as I
# was learning.

>>> 5 // 3
1
>>> 5 / 3
1.6666666666666667
>>> 5 % 3
2
>>> 5 // 3
1
>>> 5 ///3
  File "<stdin>", line 1
    5 ///3
        ^
SyntaxError: invalid syntax
>>> 2304811 // 47
49038
>>> * 47
  File "<stdin>", line 1
SyntaxError: can use starred expression only as assignment target
>>> (2304811 // 47) * 47
2304786
>>> 230811 - ( (2304811 // 47) * 47)
-2073975
>>> 2304811 - ( (2304811 // 47) * 47)
25
>>> {x^2 for x in {1,2,3,4,5}}
{0, 1, 3, 6, 7}
>>> {x*x for x in {1,2,3,4,5}}
{16, 1, 9, 25, 4}
>>> {x*x for x in {1,2,3,4,5}}
{16, 1, 9, 25, 4}
>>> {2*x for x in {1,2,3} }
{2, 4, 6}
>>> {2*x for x in {1,2,3}}
{2, 4, 6}
>>> {2*x for x in {1,2,3,4,5}}
{8, 2, 10, 4, 6}
>>> {2*x for x in {1,2,3,4,5}}
{8, 2, 10, 4, 6}
>>> {2*x for x in {1,2,3}}
{2, 4, 6}
>>> {math.pow(2,x) for x in {0,1,2,3,4}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <setcomp>
NameError: name 'math' is not defined
>>> import math
>>> {math.pow(2,x) for x in {0,1,2,3,4}}
{8.0, 1.0, 2.0, 16.0, 4.0}
>>> {math.pow(2,x) for x in {0,1,2}}
{1.0, 2.0, 4.0}
>>> s = {1,2,3,4}
>>> x for x in s
  File "<stdin>", line 1
    x for x in s
        ^
SyntaxError: invalid syntax
>>> {x for x in s}
{1, 2, 3, 4}
>>> {x*2 for x in s}
{8, 2, 4, 6}
>>> s = [1,2,3]
>>> {x*2 for x in s}
{2, 4, 6}
>>> s = {1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> {2*x for s | {5,6}}
  File "<stdin>", line 1
    {2*x for s | {5,6}}
                      ^
SyntaxError: invalid syntax
>>> {2*x for x in s | {5,6}}
{2, 4, 6, 8, 10, 12}
>>> s
{1, 2, 3, 4}
>>> {x*y for x in {1,2,3} for y in {4,5,6}}
{4, 5, 6, 8, 10, 12, 15, 18}
>>> {}
{}
>>> set()
set()
>>> s
{1, 2, 3, 4}
>>> s[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object does not support indexing
>>> s = [0,1,3,4]
>>> s[0]
0
>>> s[1]
1
>>> s[1:len(s)]
[1, 3, 4]
>>> s[0:len(s)]
[0, 1, 3, 4]
>>> s[0:len(s)+1]
[0, 1, 3, 4]
>>> s[:2]
[0, 1]
>>> s[2:]
[3, 4]
>>> [x] = [1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 1)
>>> [x,y] = [1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: need more than 1 value to unpack
>>> [x]=2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> [x]=[2]
>>> x
2
>>> s = [x]
>>> s
[2]
>>> x
2
>>> x = 2+3
>>> s
[2]
>>> x
5
>>> s = ([x]=[2])
  File "<stdin>", line 1
    s = ([x]=[2])
            ^
SyntaxError: invalid syntax
>>> (i for i in [1,3,4])
<generator object <genexpr> at 0x7f8406723dc8>
>>> s = (1 for i in [1,2,3])
>>> s
<generator object <genexpr> at 0x7f8406723cf0>
>>> s[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
>>> s
<generator object <genexpr> at 0x7f8406723cf0>
>>> s(100)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not callable
>>> sum(s)
3
>>> s
<generator object <genexpr> at 0x7f8406723cf0>
>>> s = (i for i in [1,2,3])
>>> sum(s)
6
>>> s*2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'generator' and 'int'
>>> mean(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mean' is not defined
>>> average(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'average' is not defined
>>> ave(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ave' is not defined
>>> count(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> count(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'count' is not defined
>>> 2%2 == 1
False
>>> 2%2 = 1
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> [x%2 == 1 for x in range(99)]
[False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
>>> [x for x in range(99) if x%2 == 1
... ]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]
>>> range(1:2)
  File "<stdin>", line 1
    range(1:2)
           ^
SyntaxError: invalid syntax
>>> range(1,2)
range(1, 2)
>>> range(1,5)
range(1, 5)
>>> range(5)
range(0, 5)
>>> list(range(10,15))
[10, 11, 12, 13, 14]
>>> s = zip([1,2,3],[4,5,6])
>>> s[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'zip' object is not subscriptable
>>> s
<zip object at 0x7f8406735608>
>>> L = ['a','b','c','d','e']
>>> zip(list(range(0,4)),L)
<zip object at 0x7f8406735588>
>>> len(zip)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'type' has no len()
>>> a = zip(list(range(0,4)),L)
>>> len(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'zip' has no len()
>>> a[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'zip' object is not subscriptable
>>> a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'zip' object is not subscriptable
>>> len(a[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'zip' object is not subscriptable
>>> list(a)
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
>>> a = range(0,4)
>>> a
range(0, 4)
>>> {x for x in a}
{0, 1, 2, 3}
>>> dictionary = {'a':0, 'b':1}
>>> dictionary['a]
  File "<stdin>", line 1
    dictionary['a]
                 ^
SyntaxError: EOL while scanning string literal
>>> dictionary['a']
0
>>> dictionary.keys()
dict_keys(['a', 'b'])
>>> dictionary.values()
dict_values([0, 1])
>>> dictionary.items()
dict_items([('a', 0), ('b', 1)])
>>> def twice(x): return 2*x
... 
>>> twice(2)
4
>>> def nextInts(L) : 
... return {x+1 for x in L}
  File "<stdin>", line 2
    return {x+1 for x in L}
         ^
IndentationError: expected an indented block
>>> def nextInts(L) : return {x+1 for x in L}
... 
>>> nextInts([1,3,4])
{2, 4, 5}
>>> nextInts({1,3,4})
{2, 4, 5}
>>> def nextInts(L) : return {x+1 for x in L if L == list(L)}
... 
>>> nextInts([1,3])
{2, 4}
>>> nextInts({1,3})
set()
n expects a list'L) : return {x+1 for x in L} if L == list(L) else 'This functio 
... 
>>> nextIns([1,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nextIns' is not defined
>>> nextInts([1,3,4])
{2, 4, 5}
>>> nextInts({1,3,4})
'This function expects a list'
>>> def all_3(base, digits) : return set(range(pow(base,3)))
... 
>>> all_3(2, {0,1})
{0, 1, 2, 3, 4, 5, 6, 7}
>>> all_3(2, {0})
{0, 1, 2, 3, 4, 5, 6, 7}
