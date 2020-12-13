def get_add_to(numbers, total):
    inverses = set(total-n for n in numbers)
    return list(inverses.intersection(numbers))

def part1(input, num):
    nums = [int(x) for x in input.strip().split()]
    for i in range(num+1, len(nums)):
        res = get_add_to(nums[i-num:i], nums[i])
        if len(res) == 0:
            return nums[i]


def part2(input, sumto):
    nums = [int(x) for x in input.strip().split()]
    low = 0
    high = 0
    total = 0
    while total != sumto:
        if total > sumto:
            total -= nums[low]
            low += 1
        else:
            total += nums[high]
            high += 1
    consecutive = nums[low:high]
    return max(consecutive) + min(consecutive)

test = part1(open('test.txt').read(), 5)
real = part1(open('real.txt').read(), 25)
print(real)

part2(open('test.txt').read(), test)
part2(open('real.txt').read(), real)
