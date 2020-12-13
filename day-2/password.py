import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()

num_success = 0

for line in lines:
    line = line.strip()
    rule, password = line.split(': ')
    nums, letter = rule.split()
    start, end = nums.split('-')
    start, end = int(start), int(end)
    start_match = password[start-1] == letter
    end_match = password[end-1] == letter
    if start_match != end_match:
        num_success += 1
print(num_success)

