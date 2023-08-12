def get_ranges(sorted_list):
    ranges = []
    start = sorted_list[0]
    end = sorted_list[0]

    for num in sorted_list[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = end = num

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")

    return ", ".join(ranges)

numbers1 = [0, 1, 2, 3, 4, 7, 8, 10]
print(get_ranges(numbers1))  

numbers2 = [4, 7, 10]
print(get_ranges(numbers2))  

numbers3 = [2, 3, 8, 9]
print(get_ranges(numbers3))  
