"""5. Write a function that takes an ordered list of numbers
 without duplicates and returns a string with ranges for those numbers, check the example below:
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
"""

examples = [[0, 1, 2, 3, 4, 7, 8, 10], [4, 7, 10], [2, 3, 8, 9]]


def get_ranges(nums):
    i = 0
    ans = ''
    while i < len(nums):
        st = nums[i]
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        end = nums[i]

        if st == end:
            ans = ans + ', ' + str(st)
        else:
            ans = ans + ', ' + str(st) + '-' + str(end)
        i += 1
    return ans[2:]


for example in examples:
    print(get_ranges(example))

