 - 变量拆分迭代元组或列表序列：
```
In [27]: seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
In [28]: for a, b, c in seq:
   ....:     print('a={0}, b={1}, c={2}'.format(a, b, c))
a=1, b=2, c=3
a=4, b=5, c=6
a=7, b=8, c=9
```
-  `*rest`
	从元组的开头“摘取”几个元素。
	在函数签名中以抓取任意长度列表的位置参数
```
In [29]: values = 1, 2, 3, 4, 5

In [30]: a, b, *rest = values

In [31]: a, b
Out[31]: (1, 2)

In [32]: rest
Out[32]: [3, 4, 5]
```
- `tuple/list.count()` 统计某个值得出现频率

- `list`实体化迭代器或生成器
```
In [42]: gen = range(10)

In [43]: gen
Out[43]: range(0, 10)

In [44]: list(gen)
Out[44]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
- 如果已经定义了一个列表，用`extend`方法可以追加多个元素：
```
In [58]: x = [4, None, 'foo']

In [59]: x.extend([7, 8, (2, 3)])

In [60]: x
Out[60]: [4, None, 'foo', 7, 8, (2, 3)]
```
- `sort`有一些选项，有时会很好用。其中之一是二级排序key，可以用这个key进行排序。例如，我们可以按长度对字符串进行排序：
```
In [64]: b = ['saw', 'small', 'He', 'foxes', 'six']

In [65]: b.sort(key=len)

In [66]: b
Out[66]: ['He', 'saw', 'six', 'small', 'foxes']
```
- `bisect`模块支持二分查找，和向已排序的列表插入值。`bisect.bisect`可以找到插入值后仍保证排序的位置，`bisect.insort`是向这个位置插入值
```
In [67]: import bisect

In [68]: c = [1, 2, 2, 2, 3, 4, 7]

In [69]: bisect.bisect(c, 2)
Out[69]: 4

In [70]: bisect.bisect(c, 5)
Out[70]: 6

In [71]: bisect.insort(c, 6)

In [72]: c
Out[72]: [1, 2, 2, 2, 3, 4, 6, 7]
```
- 切片的起始元素是包括的，不包含结束元素。因此，结果中包含的元素个数是`stop - start`
- 在第二个冒号后面使用step，可以隔一个取一个元素
```
In [81]: seq[::2]
Out[81]: [7, 3, 3, 6, 1]
```
- 一个聪明的方法是使用-1，*它可以将列表或元组颠倒过来*
```
In [82]: seq[::-1]
Out[82]: [1, 0, 6, 5, 3, 6, 3, 2, 7]
```
- 当你索引数据时，使用enumerate的一个好方法是计算序列（唯一的）dict映射到位置的值
```
In [83]: some_list = ['foo', 'bar', 'baz']

In [84]: mapping = {}

In [85]: for i, v in enumerate(some_list):
   ....:     mapping[v] = i

In [86]: mapping
Out[86]: {'bar': 1, 'baz': 2, 'foo': 0}
```
- `zip`的常见用法之一是同时迭代多个序列，可能结合enumerate使用：
```
In [95]: for i, (a, b) in enumerate(zip(seq1, seq2)):
   ....:     print('{0}: {1}, {2}'.format(i, a, b))
   ....:
0: foo, one
1: bar, two
2: baz, three
```
- `reversed`可以从后向前迭代一个序列：
```
In [100]: list(reversed(range(10)))
Out[100]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
- 将两个序列配对组合成字典。下面是一种写法：
```
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
```
- 集合是无序的不可重复的元素的集合。你可以把它当做字典，但是只有键没有值。可以用两种方式创建集合：通过`set`函数或使用尖括号`set`语句：
```
In [133]: set([2, 2, 2, 1, 3, 3])
Out[133]: {1, 2, 3}

In [134]: {2, 2, 2, 1, 3, 3}
Out[134]: {1, 2, 3}
```