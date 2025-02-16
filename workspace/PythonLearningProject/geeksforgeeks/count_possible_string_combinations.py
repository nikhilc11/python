#######################################################################################################################
# Given a length n, count the number of strings of length n that can be made using ‘a’, ‘b’ and ‘c’
# with at most one ‘b’ and two ‘c’s allowed.
#######################################################################################################################
#
# 0 1 2 - 19 / 27
#
# a a a - 1
# a a b - 1
# a a c - 1
# a b a - 1
# a b b - 0
# a b c - 1
# a c a - 1
# a c b - 1
# a c c - 1
#
# b a a - 1
# b a b - 0
# b a c - 1
# b b a - 0
# b b b - 0
# b b c - 0
# b c a - 1
# b c b - 0
# b c c - 1
#
# c a a - 1
# c a b - 1
# c a c - 1
# c b a - 1
# c b b - 0
# c b c - 1
# c c a - 1
# c c b - 1
# c c c - 0
#
#######################################################################################################################

def add_element_to_string(curr_string, max_string_length, elements_dict, results_set):
    elements = list(elements_dict.keys())

    for i in range(len(elements)):

        if len(curr_string) < max_string_length:
            add_element_to_string(curr_string + elements[i], max_string_length, elements_dict, results_set)

        elif len(curr_string) == max_string_length:
            validation_success_count = 0
            for j in range(len(elements)):
                if ((elements_dict[elements[j]] <= 0) or
                        (elements_dict[elements[j]] > 0 and
                         curr_string.count(elements[j]) <= elements_dict[elements[j]])):
                    validation_success_count += 1

            if validation_success_count == len(elements):
                results_set.add(curr_string)


elements_dict_to_max_possible_count = {'a': 0, 'b': 1, 'c': 2}
length_of_strings_to_be_generated = 3
count_of_elements_satisfying_condition = 0
empty_string = ''
result_set = set()
add_element_to_string(empty_string, length_of_strings_to_be_generated, elements_dict_to_max_possible_count, result_set)

print(len(result_set))

for entry in result_set:
    print(entry)

#######################################################################################################################
