# 20个问题和处理方式
from collections import deque


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


# 序列分解
# todo：赋值多个变量->可以使用在循环里，但是需要做些判断提高冗余
def func_1():
    data = [1, 2, 3, (4, 5, 6)]
    _, n1, n2, _ = data
    print(f'n1,n2分别为：{n1},{n2}')

    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(name, email, phone_numbers)

    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing, current)

    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)


# 返回满足条件的文本，并返回一个deque，存储之前查询的几列数据
def search(lines, pattern, history=5):
    prvious_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prvious_lines
        prvious_lines.append(line)


# 队列的使用->在列表的开头插入数据复杂度为O(N)
# 保留最后N个元素
def func_2_deque():
    print('func_2_deque:')
    with open(r'storage/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


import heapq


# 查找最大或最小的N个元素;
# todo：可以用于筛选集合构成的列表，筛选满足的值
def func_3_heapq():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 优先级，index数，同等优先级时的排序，录入的数据
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1  # 不加这个，同优先级会报错

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # 调用字符的时候会使用这个方法
        # 不太看得懂咯
        return 'Item({!r})'.format(self.name)


# todo:优先级队列->heqpq，填进去的东西需要能够进行比较。且不会出现相等的情况
def func_4_priority_heapq():
    q = PriorityQueue()
    q.push(Item(42), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q._queue)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


from collections import OrderedDict


def order_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    for key in d:
        print(key, d[key])


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 保留顺序删除重复值，只能手动构建函数了。
def func_5_deque():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe_2(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe_2(a, key=lambda d: d['x'])))


# todo:命名切片，以及调整长度防止抛出异常。怎么引用就很离谱了
def func_6_slice():
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)  # 左闭右开，老传统了
    print("切片部分展示  :", items[a])
    items[a] = [10, 11]
    print("修改切片部分后:", items)
    del items[a]
    print("删除切片部分后:", items)

    a = slice(5, 50, 2)
    print(a.start, a.stop, a.step)

    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


def func_13_sort():
    from operator import itemgetter

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)


# 序列中出现次数最多的元素-> Counter ，还能做运算
# 通过某个关键字排序一个字典的列表 itemgetter
# 排序不支持原生比较的对象  operator.attrgetter()


# todo:分组，一定要排序再分组
def func_15_groupby():
    from itertools import groupby
    from operator import itemgetter

    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    rows.sort(key=itemgetter('date'))
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


def func_18_namedtuple():
    from collections import namedtuple
    Subscriber = namedtuple('ttttt', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print(sub)
    print(sub.addr, sub.joined)
    sub_1, sub_2 = sub
    print(sub_1, sub_2)


def func_19_sum():
    nums = [1, 2, 3, 4, 5]
    s = sum(x * x for x in nums)  # 和 s = sum([x * x for x in nums]) 等效，效率还更高
    print(s)

    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(portfolio, key=lambda s: s['shares'])
    print(min_shares)

# func_1()
# func_2_deque()
# func_3_heapq()
# func_4_priority_heapq()
# order_dict()
# func_5_deque()
# func_6_slice()
# func_13_sort()
# func_15_groupby()
# func_18_namedtuple()
func_19_sum()
