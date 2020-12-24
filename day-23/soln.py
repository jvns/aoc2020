import sys
from dataclasses import dataclass
from typing import List
from collections import deque

@dataclass
class LL:
    value: int
    next: object

@dataclass
class Circle:
    current: object
    items: object
    max_value: int

    @staticmethod
    def create(nums):
        lls = [LL(n, None) for n in nums]
        d = {}
        for i, n in enumerate(lls):
            d[n.value] = n
            if i == len(nums) - 1:
                lls[i].next = lls[0]
            else:
                lls[i].next = lls[i+1]
        return Circle(lls[0], d, max(nums))

    def step(self):
        n = self.current.next
        nexts = [n.value, n.next.value, n.next.next.value]
        dest = (self.current.value - 2) % self.max_value + 1
        while dest in nexts:
            dest = (dest - 2) % self.max_value + 1
        target = self.items[dest]

        self.current.next = self.current.next.next.next.next
        n.next.next.next = target.next
        target.next = n
        self.current = self.current.next

    def __str__(self):
        start = self.current
        items = []
        items.append(str(start.value))
        x = start.next
        while x is not start:
            items.append(str(x.value))
            x = x.next
        return ' '.join(items)


    def result(self):
        start = self.items[1]
        items = []
        x = start.next
        while x != start:
            items.append(str(x.value))
            x = x.next
        return ''.join(items)

def part1(input):
    nums = [int(x) for x in input]
    nums = nums + list(range(max(nums)+1, 1000 * 1000  +1))
    circle = Circle.create(nums)
    for i in range(100):
        circle.step()
    print(circle.result())
part1(sys.stdin.read().strip())
