def function_that_takes_an_ordered_list_of_numbers_without_duplicates_and_returns_a_string_with_ranges_for_those_numbers(list):

    testing_list = []
    final_list = []
    testing_list.append((str(list[0])))
    list.append(list[len(list)-1])

    if list[0] + 1 != list[1]:
        list.insert(0, list[0])

    for i in range(1, len(list)-1):
        if list[i] - 1 == list[i-1] and list[i] + 1 == list[i+1]:
            continue

        elif list[i] - 1 == list[i-1] and list[i] + 1 != list[i+1]:
            testing_list.append(str(list[i]))
            final_list.append('-'.join(testing_list))
            testing_list.clear()

        elif list[i] - 1 != list[i-1] and list[i] + 1 == list[i+1]:
            testing_list.append(str(list[i]))

        elif list[i] - 1 != list[i-1] and list[i] + 1 != list[i+1]:
            final_list.append(str(list[i]))
    print(final_list)

listers = [0, 1, 2, 3, 4, 7, 8, 10]
list1 = [2, 3, 8, 9]
list2 = [4,7,10]

function_that_takes_an_ordered_list_of_numbers_without_duplicates_and_returns_a_string_with_ranges_for_those_numbers(listers)
function_that_takes_an_ordered_list_of_numbers_without_duplicates_and_returns_a_string_with_ranges_for_those_numbers(list1)
function_that_takes_an_ordered_list_of_numbers_without_duplicates_and_returns_a_string_with_ranges_for_those_numbers(list2)