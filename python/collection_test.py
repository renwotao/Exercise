#! /usr/bin/env python3
# -*- coding: utf-8 -×-

'''
	namedtuple
		tuple 可以表示不变集合，但很难看出这个 tuple 用来表示一个坐标
'''
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

'''
	namedtuple 是一个函数，它用来创建一个自定义的tuple队象，
	并且规定了 tuple 元素的个数，并可以用属性而不是索引来引用 tuple 的某个元素
'''
print(isinstance(p, Point))
print(isinstance(p, tuple))

# namedtuple('名称', [属性list])
# 用坐标和半径表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

'''
	deque
		deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

'''
	deque 实现list的 append() 和 pop() 外，还支持 appendleft() 和 popleft(),
	这样可以非常高效地往头部添加或删除元素
'''

'''
	defaultdict
		使用 dict 时，如果引用的 Key 不存在，就会抛出 KeyError。
		如果希望 Key 不存在时，返回一个默认值，就可以用 defaultdict。
'''

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

'''
	注意默认值是调用函数返回的，而函数在创建 defaultdict 对象时传入。
	除了在 Key 不存在时返回默认值，defaultdict的其他行为跟 dict 是完全一样的
'''

'''
	OrderedDict
		使用 dict 时，Key是无序的。在对 dict 做迭代时，无法确定Key的顺序
		如果要保持 Key 的顺序，可以用 OrderedDict
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict 的 Key 是无序的
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict 的 Key 是有序的
print(od)

# 注意，OrderedDict 的 Key 会按照插入的顺序排序，不是 Key 本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
# 按照插入的 Key 的顺序返回
print(list(od.keys()))

'''
	OrderedDict 可以使用一个 FIFO（先进先出）的 dict，当容量超出限制时，
	先删除最早添加的 Key
'''
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
	
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			print('remove:', last)
		if containsKey:
			del self[key]
			print('set:', (key, value))
		else:
			print('add:' (key, value))
		OrderedDict.__setitem__(self, key, value)


'''
	Counter
		简单的计数器
'''
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)

'''
	Counter 实际上是一个dict的子一个子类
'''



