import functools
import heapq
import html
import sys

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

def make_element(name, value, **attrs):
    keyvals = [' %s="%s' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, 
    value=html.escape(value))
    return element

def log(text=None):
    if text is None:
        text = ''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('{}{}()'.format(text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log()
def now():
    return '2018-08-02'

@log('calling ')
def time():
    return '17:16'

class ClosureInstane:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        
        self.__dict__.update((key,value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstane()

class Student(object):
    
    @property
    def score(self):
        if not hasattr(self, '_score'):
            return 'No data!'
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value 

if __name__ == '__main__':
    '''
    a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    

    s = Stack()
    s.push(10)
    s.pop()
    '''