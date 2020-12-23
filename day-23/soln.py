import sys
from dataclasses import dataclass
from typing import List
from collections import deque

@dataclass
class Circle:
    nums: object
    max_val: int

    def remove(self):
        num = self.nums[1]
        del self.nums[1]
        return num

    def step(self):
        cups = [self.remove() for i in range(3)]
        dest = self.nums[0]
        dest = (dest - 2) % (self.max_val) + 1
        while dest not in self.nums:
            dest = (dest - 2) % self.max_val + 1
        idx = self.nums.index(dest)
        self.nums = deque(list(self.nums)[:idx+1] + cups + list(self.nums)[idx+1:])
        self.nums.append(self.nums.popleft())

    def result(self):
        d = self.nums.copy()
        while d[0] != 1:
            d.append(d.popleft())
        return ''.join([str(x) for x in list(d)[1:]])

    def __str__(self):
        return str(self.nums)


def part1(input):
    nums = deque([int(x) for x in input])
    circle = Circle(nums, max(nums))
    for i in range(100):
        circle.step()
    print(circle.result())
part1(sys.stdin.read().strip())
