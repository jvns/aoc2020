import sys


#    If that was the first time the number has been spoken, the current player
#    says 0.  Otherwise, the number had been spoken before; the current player
#    announces how many turns apart the number is from when it was previously
#    spoken.

def part1(input):
    nums = [int(x) for x in input.split(',')]
    i = 3
    last_spoken = {}
    for i, n in enumerate(nums):
        last_spoken[n] = i
    prev = nums[-1]
    for i in range(len(nums)-1, 30000000 ):
        if prev in last_spoken:
            n = i - last_spoken[prev]
        else:
            n = 0
        last_spoken[prev] = i
        prev = n
        if (i == 30000000 - 2):
            print(n)


part1(sys.stdin.read().strip())
