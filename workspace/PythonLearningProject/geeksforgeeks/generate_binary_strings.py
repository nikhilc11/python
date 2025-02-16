#######################################################################################################################
# Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, generate all binary strings that can be formed by
# replacing each wildcard character by ‘0’ or ‘1’.
#######################################################################################################################

result = []

def generate_binary_string(binary_string):
    if '?' in binary_string:
        generate_binary_string(binary_string.replace('?','0',1))
        generate_binary_string(binary_string.replace('?','1',1))
    else:
        result.append(binary_string)

generate_binary_string('1??0?101')

{print(entry) for entry in result}
