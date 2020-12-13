from collections import Counter

def part1(input):
    nums = [int(x) for x in input.strip().split()]
    nums = [0] + nums + [max(nums)+3]
    nums = sorted(nums)
    nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    counts = Counter(nums)
    print(counts[1] * counts[3])


def part2(input):
    nums = [int(x) for x in input.strip().split()]
    nums = sorted([0] + nums + [max(nums)+3])
    num_reverse = {i: n for n, i in enumerate(nums)}
    memo = {0: 1}
    for i, num in list(enumerate(nums))[1:]:
        memo[i] = 0
        for diff in [1,2,3]:
            if num - diff in num_reverse:
                memo[i] += memo[num_reverse[num-diff]]
    print(memo[len(nums)-1])

print ('part 1')
part1(open('test.txt').read())
part1(open('test2.txt').read())
part1(open('real.txt').read())

print ('')
print ('part 2')
part2(open('test.txt').read())
part2(open('test2.txt').read())
part2(open('real.txt').read())
