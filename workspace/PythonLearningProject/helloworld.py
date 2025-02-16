#######################################################################################################################
# Comments Section
#######################################################################################################################

# This is a Comment

"""
This
is
also
a
Multiline
Comment
"""

# This Is A
# Multiline Comment

"""
This is also 
a Multiline Comment
"""

#######################################################################################################################
# Hello World
#######################################################################################################################

print('Hello World!')

#######################################################################################################################
# Assignments and Numeric Operations
#######################################################################################################################

print("Assignments and Numeric Operations")

c, d = "Nikhil", "Shilpa"

print(c)
print(type(c))
print(d)
print(type(d))

e = f = g = "Love"

print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))

coll = ["Shilpa", "Loves", "Nikhil"]

x, y, z = coll

print(z)
print(type(z))
print(y)
print(type(y))
print(x)
print(type(x))

#######################################################################################################################
# Notes
#######################################################################################################################
"""
DataTypes:
    Text (String are Arrays)
        Str                                             = "Text Type"
    Numeric
        int         (replaces long -> No Limit in Size) = 20
        float       (real numbers with fractional part) = 5.5
        decimal     (higher precision)                  = 5.5
        complex     (sqrt -1 -> a+bj)                   = 5+1j
    Iterator
        ???
    Sequence(like Iterators - Ordered)
        list                                            = ["apple", "banana", "cherry"]
        tuple                                           = ("username@provider.com", 9876543210,"Full Name")
        range                                           = range(6)
    Mapping
        dict = {"email_id" : "username@provider.com", "mobile_number" : "9876543210", "full_name" : "Full Name"}
    Sets (UnOrdered)
        set                                             = {"apple", "banana", "cherry"}
        frozenset                                       = frozenSet(set) / frozenSet({"apple", "banana", "cherry"})
    Boolean
        bool                                            = False / True
    Binary
        bytes                                           = b"Hello"
        bytearray                                       = bytearray(5)
        memoryview                                      = memoryview(bytes(5))
    None
        NoneType                                        = None
    File
    Class
    Exception
Type Casting
    int()
    float()
    str()
"""

#######################################################################################################################
# Here are input values
#######################################################################################################################

# a = input("Please input a large number: ")
a = 11
print(a)
print(type(a))
a = int(a)
print(a)
print(type(a))

# b = input("Please input a smaller number: ")
b = 2
print(b)
print(type(b))
b = int(b)
print(b)
print(type(b))

#######################################################################################################################
# Numeric Operators Precedence (Brackets-Order-Division-Multiplication-Addition-Subtraction):
#######################################################################################################################
"""
Print out all basic 
calculator operations
"""
print("Input 1: ", a)
print("Input 2: ", b)
print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Integer Division: ", a // b)
print("Power: ", a ** b)
print("Modulo: ", a % b)

#######################################################################################################################
# Take Console Input
#######################################################################################################################

# first_name = input("Please enter your first name: ")
first_name = "Nikhil"
# last_name = input("Please enter your last name: ")
last_name = "Chadha"

#######################################################################################################################
# String Operations
#######################################################################################################################

# Error Prone code
username = first_name.strip()[0].lower() + "." + last_name.strip().lower()

# Error Safe code
username_1 = first_name.strip()[:1].lower() + "." + last_name.strip().lower()

username_secondary = first_name.strip()[0:3].lower() + "." + last_name.strip().lower()

username_tertiary_v1 = first_name.strip()[-len(first_name.strip())].upper() + "." + last_name.strip().upper()[0:4]

username_tertiary_v2 = first_name[3:].strip().upper() + "." + last_name.strip().upper()[:4]

username_step_slice = first_name.strip().upper()[0::2] + "." + last_name.strip().upper()[0::3]

print(first_name)
print(type(first_name))
print(last_name)
print(type(last_name))
print(username)
print(type(username))
print(username_1)
print(type(username_1))
print(username_secondary)
print(type(username_secondary))
print(username_tertiary_v1)
print(type(username_tertiary_v1))
print(username_tertiary_v2)
print(type(username_tertiary_v2))
print(username_step_slice)
print(type(username_step_slice))

#######################################################################################################################
# Print Hello with Input Name
#######################################################################################################################

print('Hello "' + first_name + '"!')
print("Hello '" + last_name + "'!")
print('Hello \'' + first_name + '\'!')
print("Hello \"" + last_name + "\"!")
print("""Hello '""" + username + """' to "Python World" !""")

print("""Hi Nikhil \
Can we go to the next line please. \
\n hello new line!""")

print("C:\\Users\\nikhil-chadha")
print(r"C:\Users\nikhil-chadha")

#######################################################################################################################
# String Operations - Continued
#######################################################################################################################

full_name = first_name + " " + last_name

name_array = full_name.split(" ")

print(name_array)
print(type(name_array))
print(name_array[0])
print(name_array[1])

print(full_name)
print(type(full_name))

full_username = full_name.lower().replace(" ", ".")
print(full_username)
print(type(full_username))

print(len(first_name))
print(len(last_name))
print(len(full_name))

for i in full_name.upper():
    print(i)

reverse_full_username = full_name.upper()[::-1]
print(reverse_full_username)

for i in range(len(full_name)):
    print(full_name.upper()[(-1 * i) - 1])

if first_name.lower() in username:
    print("First Name Exists in username!")
else:
    print("First Name Does Not Exist in username!")

if last_name.lower() not in username:
    print("Last Name Does Not Exist in username!")
else:
    print("Last Name Exists in username!")

#######################################################################################################################
# Printing Formatted String
#######################################################################################################################

# print(f""" With First Name provided as "{first_name}" and Last Name provided as "{last_name}" the Full Name can be \
# computed as "{full_name}" and the list of possible usernames is "{username}", "{username_secondary}", \
# "{username_tertiary_v1}", "{username_tertiary_v2}", "{username_step_slice}", "{full_username}" and \
# "{reverse_full_username}" which should be provided to the new candidate as options to make choices.""")

#######################################################################################################################
# String Functions
# LINK: https://www.w3schools.com/python/python_ref_string.asp
#######################################################################################################################

print()
print(f"Original String: {full_name}")
print(f"Capitalize: {full_name.capitalize()}")
print(f"CaseFold: {full_name.casefold()}")
print(f"Center: {full_name.center(20)}")
print(f"Count: {full_name.count('a')}")
print(f"Encode: {full_name.encode(encoding='ascii')}")
print(f"EndsWith: {full_name.casefold().endswith(last_name.casefold(), len(first_name), len(full_name))}")
print(f"ExpandTabs: {full_name.expandtabs(2)}")
# Exception Safe - Find is better than Index
print(f"Find: {full_name.casefold().find(last_name.casefold(), 0, len(full_name))}")
print(f"Find: {full_name.casefold().find(first_name.casefold(), 0, len(full_name))}")
print(f"Find: {full_name.casefold().find('a', 0, len(full_name))}")
print(f"Find: {full_name.casefold().find('i', 0, len(full_name))}")
print("Format: {0}".format(full_name))
print(f"Format: {full_name}")
print(f"Index: {full_name.casefold().index('a', 0, len(full_name))}")
print(f"Index: {full_name.casefold().index('i', 0, len(full_name))}")
print(f"IsAlNum: {full_name.isalnum()}")
print(f"IsAlpha: {full_name.isalpha()}")
print(f"IsAscii: {full_name.isascii()}")
print(f"IsDecimal: {full_name.isdecimal()}")
print(f"IsDigit: {full_name.isdigit()}")
print(f"IsIdentifier: {full_name.isidentifier()}")
print(f"IsLower: {full_name.islower()}")
print(f"IsNumeric: {full_name.isnumeric()}")
print(f"IsPrintable: {full_name.isprintable()}")
print(f"Isspace: {full_name.isspace()}")
print(f"Istitle: {full_name.istitle()}")
print(f"Isupper: {full_name.isupper()}")
print(f"LJust: {full_name.ljust(20)}")
print(f"Lower: {full_name.lower()}")
print(f"LStrip: {full_name.lstrip()}")
print(f"Partition: {full_name.partition(' ')}")
print(f"Replace: {full_name.replace(' ', '.')}")  # Replace count of instances as additional optional param
print(f"RFind: {full_name.casefold().rfind(last_name.casefold(), 0, len(full_name))}")
print(f"RFind: {full_name.casefold().rfind(first_name.casefold(), 0, len(full_name))}")
print(f"RFind: {full_name.casefold().rfind('a', 0, len(full_name))}")
print(f"RFind: {full_name.casefold().rfind('i', 0, len(full_name))}")
print(f"RIndex: {full_name.casefold().rindex('a', 0, len(full_name))}")
print(f"RIndex: {full_name.casefold().rindex('i', 0, len(full_name))}")
print(f"RJust: {full_name.rjust(20)}")
print(f"RPartition: {full_name.rpartition(' ')}")
print(f"Rsplit: {full_name.rsplit(' ')}")
print(f"RStrip: {full_name.rstrip()}")
print(f"Split: {full_name.split()}")
print(f"Splitlines: {full_name.splitlines()}")
print(f"Startswith: {full_name.casefold().startswith(first_name.casefold(), 0, len(full_name))}")
print(f"Strip: {full_name.strip()}")
print(f"SwapCase: {full_name.swapcase()}")
print(f"Title: {full_name.title()}")
print(f"Upper: {full_name.upper()}")
print(f"ZFill: {full_name.zfill(20)}")  # Zero Fills - Used for Integer based Strings Justification

# print("FormatMap: " + full_name.format_map())
# print(f"Join: {full_name.join()}")             # LINK: https://www.w3schools.com/python/ref_string_join.asp
# print(f"Maketrans: {full_name.maketrans()}")   # LINK: https://www.w3schools.com/python/ref_string_maketrans.asp
# print(f"Translate: {full_name.translate()}")   # LINK: https://www.w3schools.com/python/ref_string_translate.asp

print((full_name + "\t") * 5)

print("____________________STRING ENDS HERE_____________________________")

#######################################################################################################################
# Python Operators and Operator Precedence Order
#######################################################################################################################

"""
Python Operators:
    Arithmetic operators:
        +
        -
        *
        /
        %
        **
        //
    Assignment operators:
        =
        +=
        -=
        *=
        /=
        %=
        **=
        //=
        &=
        |=
        ^=
        >>=
        <<=
        := Assignment on the spot while using parameter
    Comparison operators:
        ==
        !=
        >
        <
        >=
        <=
    Logical operators:
        and
        or
        not
    Identity operators:
        is
        is not
    Membership operators:
        in
        not in
    Bitwise operators:
        &     Bitwise AND
        |     Bitwise OR
        ^     Bitwise XOR
        ~     Bitwise NOT
        <<    Bitwise LEFT SHIFT with 0 Fill
        >>    Bitwise Right Shift with Signed
        
"""

#######################################################################################################################
# Conditional Statement
#######################################################################################################################

# num1 = input("Please Input First Number: ")
num1 = "11"
# num2 = input("Please Input Second Number: ")
num2 = "22"

num1 = int(num1)
num2 = int(num2)

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

if num1 < num2:
    print("Swapping Numbers")
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
elif num1 == num2:
    print("Both numbers Equal")
else:
    print("Keeping the numbers unchanged")

print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

#######################################################################################################################
# While Loop Statement
#######################################################################################################################
# Note (for all loops):
#   Pass Statement (if not having any code in any section)
#   Continue Statement (Move to Next Iteration)
#   Break Statement (Exit Loop)
#   Else Statement (Runs once the loop exits & condition evaluates to false)
#######################################################################################################################

print("\n\nWhile Loop")

# loop_head = input("Please provide Loop Iteration Max Count Less Than 12: ")
loop_head = "12"
loop_head = int(loop_head)

val = 0

while val <= loop_head:

    val += 1

    if val % 5 == 0:
        continue

    if val % 12 == 0:
        break

    print(val)

else:
    print(f"Loop Completed as val = {val}")  # will be printed only in the number input is less than 11

#######################################################################################################################
# For Loop Statement
#######################################################################################################################

print("\n\nFor Loop")

username_list = [username,
                 username_secondary,
                 username_tertiary_v1,
                 username_tertiary_v2,
                 username_step_slice,
                 full_username,
                 reverse_full_username]

for string in username_list:
    print(string)
    for char in string:
        if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            break
        print(char)
else:
    print("For Loop Finished")

print("New For Loop")

for i in range(20, 0, -1):
    print(i)
else:
    print("For Loop Finished")


#######################################################################################################################
# Functions
#######################################################################################################################

def empty_function():
    pass


def say_hello_to(*, name="Chadha"):
    print("Hello" + name + "!")


say_hello_to(name="Nikhil")
say_hello_to(name="Nidhi")
say_hello_to(name="Neha")
say_hello_to(name="Shilpa")


def add_integers(*integers):
    sum = 0
    for i in integers:
        sum += i
    return sum


print(add_integers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def add_integers_in_range(integer_range, /):
    sum_val = 0
    for element in integer_range:
        sum_val += element
    return sum_val


print(add_integers_in_range(range(1, 10, 1)))


def say_hello_to_team_member(first_name, last_name, /, *, middle_name="", salutation="Mr"):
    print(f"Hello {salutation}. {first_name} {middle_name} {last_name}")


say_hello_to_team_member("Nikhil", "Chadha")
say_hello_to_team_member("Shilpa", "Chadha", middle_name="Das", salutation="Mrs")


#######################################################################################################################
# Recursion
#######################################################################################################################

def print_name_in_loop(name, times=3):
    print(name)
    times -= 1
    if times > 0:
        print_name_in_loop(name, times)
    else:
        return 0


print_name_in_loop("Nikhil")
print_name_in_loop("Shilpa", 10)


def factorial(number):
    if number < 0:
        return -1
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(-1))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))
print(factorial(11))


def print_fibonacci_series_upto_number(number):
    num_1 = num_2 = 1

    print(num_1)
    print(num_2)

    while num_1 + num_2 <= number:
        next_num = num_1 + num_2
        print(next_num)
        num_1 = num_2
        num_2 = next_num


print_fibonacci_series_upto_number(500)

#######################################################################################################################
# Lambdas
# Link: https://www.w3schools.com/python/python_lambda.asp
#######################################################################################################################

lambda_function = lambda n1, n2: n1 * n2

print(lambda_function(2, 3))

#######################################################################################################################
# Global Keyword & Python Variable Scope
# global -> Converting a variable to global from within a function
#######################################################################################################################

print("Global Variables Example")

var = 1


def my_function_1():
    var = 2
    print(var)


def my_function_2():
    global var
    var = 3
    print(var)


my_function_1()
print(var)

my_function_2()
print(var)

#######################################################################################################################
# Non-Local Keyword & Python Variable Scope
# nonlocal -> Used in Nested Functions -> Variable will start to belong to outer function
#######################################################################################################################

x = "Hi"


def my_func_1():
    x = "John"

    def my_func_2():
        nonlocal x
        x = "hello"

    my_func_2()
    return x


print(my_func_1())

print(x)

#######################################################################################################################
# Try Except Block
# LINK: https://www.w3schools.com/python/python_try_except.asp
#######################################################################################################################

# number_0001 = int(input("Please enter an integer"))
number_0001 = 97
# number_0001 = input("Please enter an integer")
number_0001 = "97"
# string_0001 = input("Please enter a String")
string_0001 = "One"

try:
    print("Now in TRY block.")
    print(string_0001 + number_0001)
except Exception:
    print("Now in EXCEPT block.")
    raise Exception("Error in Concatenation.")
else:
    print("Now in ELSE block.")
finally:
    print("Now in FINALLY block.")

#######################################################################################################################
# Collection Data Structures Differences in Python
#######################################################################################################################
# List        -> ordered      -> Add      -> Update       -> Delete       -> AllowsDuplicates
# Tuple       -> ordered      -> NoAdd    -> NoUpdate     -> NoDelete     -> AllowsDuplicates
# Set         -> unordered    -> Add      -> NoUpdate     -> Delete       -> NoDuplicates
# Dictionary  -> ordered      -> Add      -> Update       -> Delete       -> NoDuplicates
#######################################################################################################################

#######################################################################################################################
# Lists (Arrays are also implemented as lists)
# LINK: https://www.w3schools.com/python/python_lists.asp
# LINK: https://www.w3schools.com/python/python_arrays.asp
# LINK: https://www.w3schools.com/python/python_lists_exercises.asp -> Exercises
# Notes:
# List items are Ordered, Changable (using index), add/remove items & Allow Duplicates with mono & combined datatypes
#######################################################################################################################

cars = ["TATA NANO", "TATA NEXON", "TATA TIAGO NRG", "MARUTI SUZUKI ALTO K10"]

for car in cars:
    print(car)

print(len(cars))

for car_index in range(len(cars)):
    print(cars[-1 * car_index - 1])

index_2 = 0
while index_2 < len(cars):
    print(cars[index_2])
    index_2 += 1

[print(p) for p in cars]

cars.append("FORCE URBANIA")
print(cars)

cars.pop(0)
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True, key=str.lower)
print(cars)

cars.reverse()
print(cars)

#######################################################################################################################
# List Functions
# LINK: https://www.w3schools.com/python/python_ref_list.asp
# append, clear, copy, count, extend, index, insert, pop, remove, revere, sort
#######################################################################################################################

cars = list(("TATA NANO", "TATA NEXON", "TATA TIAGO NRG", "MARUTI SUZUKI ALTO K10"))
print(cars)
print(type(cars))

# Access
print(cars[1])
print(cars[-1])
print(cars[1:3])
print(cars[:3])
print(cars[3:])
print(cars[::-1])
print(cars[-1:-3])
print(cars[-3:-1])

for car in cars:
    if "TATA" in car:
        print("TATA CAR EXISTS")
        break
    else:
        print("TATA CAR NOT EXISTS")

# Insert List Items

cars.insert(0, "TVS Star City 110cc")
print(cars)

cars.insert(1, "TVS Sport 100cc")
print(cars)

cars.pop(0)
print(cars)

cars.pop(0)
print(cars)

bikes = list(("TVS Star City 110cc", "TVS Sport 100cc"))
print(bikes)

bikes.append("EMOTORAD-M2")
print(bikes)
print(type(bikes))

vehicles_v0 = bikes + cars
print(vehicles_v0)
print(type(vehicles_v0))

vehicles = bikes.copy()
vehicles = list(bikes)
vehicles = bikes[:]

print(vehicles)
print(type(vehicles))

vehicles.extend(cars)
print(vehicles)

vehicles.append(vehicles[2])
print(vehicles)

vehicles.pop(2)
print(vehicles)

del vehicles[-1]
print(vehicles)

vehicles.append(bikes[-1])
print(vehicles)

print(vehicles.count(bikes[-1]))

try:
    print("Search List started")
    print(vehicles.index(bikes[-1], 0, 7))
except Exception:
    print("Item not in Selected List Segment")
else:
    print("Item found in Selected List Segment")
finally:
    print("Search List completed")

vehicles.clear()
print(vehicles)

#######################################################################################################################
# Tuples
# LINK: https://www.w3schools.com/python/python_tuples.asp
# Link: https://www.w3schools.com/python/python_ref_tuple.asp
# Notes:
# Tuples are used to store multiple items in a single variable
# They are Unchangable (Immutable), and written with Round Brackets ()
# Tuple Items are Ordered, Unchangable, Indexed, and can contain duplicate values
#######################################################################################################################

nikhil_tuple = (1, "Nikhil Chadha", "(+91) 9876543210", "Male", True)
print(nikhil_tuple)
print(type(nikhil_tuple))
print(len(nikhil_tuple))
print(nikhil_tuple[0])
print(type(nikhil_tuple[0]))
print(nikhil_tuple[1])
print(type(nikhil_tuple[1]))
print(nikhil_tuple[2])
print(type(nikhil_tuple[2]))
print(nikhil_tuple[3])
print(type(nikhil_tuple[3]))
print(nikhil_tuple[4])
print(type(nikhil_tuple[4]))
print(nikhil_tuple[2:4])

shilpa_tuple = tuple((2, "Shilpa Das", "(+91) 9876543210", "Female", False))
print(shilpa_tuple)
print(type(shilpa_tuple))
print(len(shilpa_tuple))
print(shilpa_tuple[-1])
print(type(shilpa_tuple[-1]))
print(shilpa_tuple[-2])
print(type(shilpa_tuple[-2]))
print(shilpa_tuple[-3])
print(type(shilpa_tuple[-3]))
print(shilpa_tuple[-4])
print(type(shilpa_tuple[-4]))
print(shilpa_tuple[-5])
print(type(shilpa_tuple[-5]))
print(shilpa_tuple[-4:-2])
print(shilpa_tuple[::-1])

if False in shilpa_tuple:
    print(f"User '{shilpa_tuple[1]}' is Active in System.")

#######################################################################################################################
# To Change Tuple Elements Follow This Procedure:
# 1. Convert Tuple to List
# 2. Modify Element in List
# 3. Convert List into new Tuple
#######################################################################################################################

print(shilpa_tuple)
temp_list = list(shilpa_tuple)
temp_list[2] = "(+91) 1234567890"
temp_list[4] = True
temp_list.append("20-01-2025")
shilpa_tuple = tuple(temp_list)
print(shilpa_tuple)
temp_list = list(shilpa_tuple)
temp_list.pop(-1)
shilpa_tuple = tuple(temp_list)
print(shilpa_tuple)
shilpa_tuple += ("20-01-2025",)
print(shilpa_tuple)

print(nikhil_tuple)
nikhil_tuple += ("11-11-2024",)
print(nikhil_tuple)

# Unpacking Tuples

(p_id, p_name, p_mobile, p_gender, p_inactive, p_exit_date, *p_others) = shilpa_tuple

print(p_id)
print(type(p_id))
print(p_name)
print(type(p_name))
print(p_mobile)
print(type(p_mobile))
print(p_gender)
print(type(p_gender))
print(p_inactive)
print(type(p_inactive))
print(p_exit_date)
print(type(p_exit_date))
print(p_others)
print(type(p_others))

print(shilpa_tuple.count(True))

try:
    print("Search Tuple started")
    print(shilpa_tuple.index(True, 0, 6))
except Exception:
    print("Item not in Selected Tuple Segment")
else:
    print("Item found in Selected Tuple Segment")
finally:
    print("Search Tuple completed")

#######################################################################################################################
# Sets
# LINK: https://www.w3schools.com/python/python_sets.asp
# LINK: https://www.w3schools.com/python/python_ref_set.asp
# Notes:
# UnOrdered, Unchangable (No Modify Operation - to modify, convert to List, modify and convert back to Set), Distinct
# Only Add Operation
# Access  using loop or membership operators (in / not in)
# Set Methods:
# add, clear, copy, pop, remove, update, discard
#######################################################################################################################

fruits_set = {'apple', 'banana', 'cherry'}
fruits_set = set(('apple', 'banana', 'cherry'))
print(fruits_set)
print(type(fruits_set))
print(len(fruits_set))

fruits_set.add("mango")
print(fruits_set)
fruits_set.add("kiwi")
print(fruits_set)
fruits_set.add("orange")
print(fruits_set)

fruits_list = ["strawberry", "pineapple"]
fruits_set.update(fruits_list)
print(fruits_set)

fruits_set_updated = fruits_set.copy()

try:
    print("Remove Element started")
    fruits_set.remove("orange")
except Exception:
    print("Element Does not Exist in Set")
else:
    print("Element Removed")
finally:
    print("Remove Element completed")
    print(fruits_set)

fruits_set.discard("kiwi")
print(fruits_set)

try:
    print("Remove Element started")
    fruits_set.remove("orange")
except Exception:
    print("Element Does not Exist in Set")
else:
    print("Element Removed")
finally:
    print("Remove Element completed")
    print(fruits_set)

fruits_set.discard("kiwi")
print(fruits_set)

fruits_set.pop()
print(fruits_set)

fruits_set.pop()
print(fruits_set)

fruits_set.clear()
print(fruits_set)

del fruits_set
try:
    print("Print Set started")
    print(fruits_set)
except Exception:
    print("Set Does Not Exist")
else:
    print("Set Printed")
finally:
    print("Print Set completed")

print(fruits_set_updated)

#######################################################################################################################
# Set Join Operations and Set Validations:
# difference (-), difference_update (-=),
# intersection (&), intersection_update (&=),
# symmetric_difference (^), symmetric_difference_update (^=),
# union (|), update (|=),
# issubset (<, <=), issuperset (>, >=), isdisjoint
#######################################################################################################################
print()
print("SET OPERATIONS")
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {2, 4, 6, 8, 10, 12, 14}
set_3 = {3, 6, 9, 12, 15}
set_4 = {4, 8, 12}
set_5 = {5, 10, 15}
print()
print(f"Set_1: {set_1}")
print(f"Set_2: {set_2}")
print(f"Set_3: {set_3}")
print(f"Set_4: {set_4}")
print(f"Set_5: {set_5}")
print()
print(f"Union_1_5: {set_1 | set_5}")
print(f"Union_5_1: {set_5.union(set_1)}")
print()
print(f"Intersection_1_2: {set_1 & set_2}")
print(f"Intersection_2_1: {set_2.intersection(set_1)}")
print()
print(f"Difference_2_3: {set_2 - set_3}")
print(f"Difference_3_2: {set_3.difference(set_2)}")
print()
print(f"SymmetricDifference_2_5: {set_2 ^ set_5}")
print(f"SymmetricDifference_5_2: {set_5.symmetric_difference(set_2)}")
print()
print(f"Is_Subset_2_1: {set_2 < set_1}")
print(f"Is_Subset_4_2: {set_4.issubset(set_2)}")
print()
print(f"Is_Superset_1_3: {set_1 > set_3}")
print(f"Is_Superset_2_4: {set_2.issuperset(set_4)}")
print()
print(f"Is_Disjoint_4_5: {set_4.isdisjoint(set_5)}")
print(f"Is_Disjoint_5_4: {set_5.isdisjoint(set_4)}")
print()
set_1 |= set_2
print(f"Union_Update_1_2: {set_1}")
set_2 &= set_3
print(f"Intersection_Update_2_3: {set_2}")
set_3 -= set_5
print(f"Difference_Update_3_5: {set_3}")
set_2 ^= set_5
print(f"SymmetricDifference_Update_2_5: {set_2}")
print()
print(f"All_Union: {set_1.union(set_2, set_3, set_4, set_5)}")
print(f"All_Union: {set_1 | set_2 | set_3 | set_4 | set_5}")
print()
print(f"Set_1: {set_1}")
print(f"Set_2: {set_2}")
print(f"Set_3: {set_3}")
print(f"Set_4: {set_4}")
print(f"Set_5: {set_5}")
print()

#######################################################################################################################
# Dictionaries
# LINK: https://www.w3schools.com/python/python_dictionaries.asp
# LINK: https://www.w3schools.com/python/python_ref_dictionary.asp
# Notes:
# Stores entries in "Key" : "Value" Pairs
# Ordered
#######################################################################################################################

dict_keys = ["p_id", "p_name", "p_mobile", "p_gender", "p_inactive", "p_exit_date"]


def print_emp_dictionary(dict_name, dict_val):
    print()
    print(f"{dict_name} Dictionary - {dict_val}")
    print()
    print(f"{dict_name} Dictionary - Length - {len(dict_val)}")
    print()

    for item in dict_keys:
        if item in dict_val:
            print(f"{dict_name} Dictionary - {item} Item - {dict_val[item]}")
            print(f"{dict_name} Dictionary - Type {item} Item - {type(dict_val[item])}")
    print()

    # if dict_keys[0] in dict_val:
    #     print(f"{dict_name} Dictionary - {dict_keys[0]} Item - {dict_val[dict_keys[0]]}")
    # if dict_keys[1] in dict_val:
    #     print(f"{dict_name} Dictionary - {dict_keys[1]} Item - {dict_val[dict_keys[1]]}")
    # if dict_keys[2] in dict_val:
    #     print(f"{dict_name} Dictionary - {dict_keys[2]} Item - {dict_val[dict_keys[2]]}")
    # if dict_keys[3] in dict_val:
    #     print(f"{dict_name} Dictionary - {dict_keys[3]} Item - {dict_val[dict_keys[3]]}")
    # if dict_keys[4] in dict_val:
    #     print(f"{dict_name} Dictionary - {dict_keys[4]} Item - {dict_val[dict_keys[4]]}")
    # if dict_keys[5] in dict_val:
    #     print(f"{dict_name} Dictionary - {dict_keys[5]} Item - {dict_val[dict_keys[5]]}")
    # print()

    # if dict_keys[0] in dict_val:
    #     print(f"{dict_name} Dictionary - Type {dict_keys[0]} Item - {type(dict_val[dict_keys[0]])}")
    # if dict_keys[1] in dict_val:
    #     print(f"{dict_name} Dictionary - Type {dict_keys[1]} Item - {type(dict_val[dict_keys[1]])}")
    # if dict_keys[2] in dict_val:
    #     print(f"{dict_name} Dictionary - Type {dict_keys[2]} Item - {type(dict_val[dict_keys[2]])}")
    # if dict_keys[3] in dict_val:
    #     print(f"{dict_name} Dictionary - Type {dict_keys[3]} Item - {type(dict_val[dict_keys[3]])}")
    # if dict_keys[4] in dict_val:
    #     print(f"{dict_name} Dictionary - Type {dict_keys[4]} Item - {type(dict_val[dict_keys[4]])}")
    # if dict_keys[5] in dict_val:
    #     print(f"{dict_name} Dictionary - Type {dict_keys[5]} Item - {type(dict_val[dict_keys[5]])}")
    # print()

    # print(f"{dict_name} Dictionary - Keys - {dict_val.keys()}")
    # print()

    # print(f"{dict_name} Dictionary - Values - {dict_val.values()}")
    # print()

    # print(f"{dict_name} Dictionary - Items - {dict_val.items()}")
    # print()

    # for key in dict_val.keys():
    #     print(key)
    # print()

    # for value in dict_val.values():
    #     print(value)
    # print()

    # for item in dict_val.items():
    #     print(item)
    # print()


print()
print("Dictionaries")
print()

nikhil_dict = dict.fromkeys(dict_keys)

print_emp_dictionary("Nikhil", nikhil_dict)

nikhil_dict[dict_keys[0]] = 1
nikhil_dict[dict_keys[1]] = "Nikhil Chadha"
nikhil_dict[dict_keys[2]] = "(+91) 9876543210"
nikhil_dict[dict_keys[3]] = "Male"
nikhil_dict[dict_keys[4]] = True
nikhil_dict[dict_keys[5]] = "11-11-2024"

# nikhil_dict = {
#     "p_id": 1,
#     "p_name": "Nikhil Chadha",
#     "p_mobile": "(+91) 9876543210",
#     "p_gender": "Male",
#     "p_inactive": True,
#     "p_exit_date": "11-11-2024"
# }

print_emp_dictionary("Nikhil", nikhil_dict)

shilpa_dict = dict(p_id=2, p_name="Shilpa Das", p_mobile="(+91) 1234567890", p_gender="Female", p_inactive=False)
print_emp_dictionary("Shilpa", shilpa_dict)

shilpa_dict_v2 = shilpa_dict.copy()
print_emp_dictionary("Shilpa", shilpa_dict_v2)

shilpa_dict_v2["p_inactive"] = True
shilpa_dict_v2["p_exit_date"] = "20-01-2025"
print_emp_dictionary("Shilpa", shilpa_dict_v2)

shilpa_dict_v2.update({"p_inactive": False})
shilpa_dict_v2.update({"p_exit_date": ""})
shilpa_dict_v2.update({"p_location": "Bangalore"})

print_emp_dictionary("Shilpa", shilpa_dict_v2)

nikhil_dict["p_location"] = "Bangalore"
print_emp_dictionary("Nikhil", nikhil_dict)

shilpa_dict_v2.pop("p_inactive")
print_emp_dictionary("Shilpa", shilpa_dict_v2)

del nikhil_dict["p_inactive"]
print_emp_dictionary("Nikhil", nikhil_dict)

#######################################################################################################################
# Performing Sort on Keys and Values in Dictionary
# Set Changes the Order of List Items
# Dictionary Maintains the Order of List Items
#######################################################################################################################


#######################################################################################################################
# Performing Distinct of a List
# Set Changes the Order of List Items
# Dictionary Maintains the Order of List Items
#######################################################################################################################

print("List DeDuplicate Operation")

fruits_list = ['apple', 'banana', 'cherry', 'apple', 'mango', 'orange', 'mango', 'strawberry']
print(fruits_list)

fruits_set = set(fruits_list)
print(fruits_set)

fruits_list_distinct = list(fruits_set)
print(fruits_list_distinct)

fruits_dict = dict().fromkeys(fruits_list)
print(fruits_dict)

fruits_list_distinct = list(fruits_dict)
print(fruits_list_distinct)

#######################################################################################################################
# Built-in Functions
# LINK: https://www.w3schools.com/python/python_ref_functions.asp
#######################################################################################################################

print(f"ABS Function - {abs(-234)}")
print(f"HEX Function - {hex(16)}")
print(f"OCT Function - {oct(16)}")
print(f"MAX Function - {max(5, 3, 4, 7, 1, 6, 3, 9, 7, 2, 5, 8)}")
print(f"MIN Function - {min(5, 3, 4, 7, 1, 6, 3, 9, 7, 2, 5, 8)}")
print(f"POW Function - {pow(2, 10, 5)}")
print(f"ROUND Function - {round(3.143526578, 2)}")
print(f"ROUND Function - {round(123453, -2)}")

exec('variable="VARIABLE"\nprint(f" EXEC Function - {variable}")')

print(f"RANGE Function - {range(100, 1, -20)}")
for i in range(100, 1, -20):
    print(i)


def print_list(list_var):
    for item in list_var:
        print(item)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_list_reversed = reversed(numbers_list)
print(f"REVERSED Function - ")
print_list(numbers_list_reversed)

numbers_list.reverse()
numbers_list_reversed = reversed(numbers_list)
print(f"REVERSED Function - ")
print_list(numbers_list_reversed)

numbers_list.reverse()
sl = slice(6)
print(f"SLICE Function - {numbers_list[sl]}")
sl = slice(6, 10)
print(f"SLICE Function - {numbers_list[sl]}")
sl = slice(-100, -1, 3)
print(f"SLICE Function - {numbers_list[sl]}")
sl = slice(4, 10, 2)
print(f"SLICE Function - {numbers_list[sl]}")
print(f"SUM Function - {sum(numbers_list)}")
print(f"SUM Function - {sum(numbers_list, 10)}") # sum with 10 as init value
numbers_list.reverse()
print(f"SORTED Function - {numbers_list}")
print(f"SORTED Function - {sorted(numbers_list)}")
numbers_list.reverse()
print(f"SORTED Function - {numbers_list}")
print(f"SORTED Function - {sorted(numbers_list, reverse=True)}")
cars_list = ['TVS Star City 110cc', 'TVS Sport 100cc', 'TATA NANO', 'TATA NEXON',
             'TATA TIAGO NRG', 'MARUTI SUZUKI ALTO K10', 'EMOTORAD-M2']
print(f"SORTED Function - {sorted(cars_list)}")
print(f"SORTED Function - {sorted(cars_list, key=len)}")

#######################################################################################################################
# Classes and Objects
# LINK: https://www.w3schools.com/python/python_classes.asp
#######################################################################################################################
pass

#######################################################################################################################
# Inheritance
# LINK: https://www.w3schools.com/python/python_inheritance.asp
#######################################################################################################################
pass

#######################################################################################################################
# Iterators
# LINK: https://www.w3schools.com/python/python_iterators.asp
#######################################################################################################################

my_fruits_list = ["apple", "banana", "cherry"]

my_list_iterator = iter(my_fruits_list)

x = next(my_list_iterator)
print(x)
x = next(my_list_iterator)
print(x)
x = next(my_list_iterator)
print(x)

pass
#######################################################################################################################
# Performing Sort on Keys and Values in Dictionary
# Set Changes the Order of List Items
# Dictionary Maintains the Order of List Items
#######################################################################################################################

# Performing Sort on Keys

student_dict = {'ravi': 10, 'rajnish': 12, 'sanjeev': 15}

print(student_dict)

student_dict_keys = student_dict.keys()
student_dict_keys = sorted(student_dict_keys)
student_dict_sorted = {i:student_dict[i] for i in student_dict_keys}
print(student_dict_sorted)

student_dict_keys = student_dict.keys()
student_dict_keys = sorted(student_dict_keys, reverse=True)
student_dict_sorted = {i:student_dict[i] for i in student_dict_keys}
print(student_dict_sorted)

student_dict_values_sorted = dict(sorted(student_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=False))
print(student_dict_values_sorted)

student_dict_values_sorted_rev = dict(sorted(student_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
print(student_dict_values_sorted_rev)


#######################################################################################################################
# Polymorphism
# LINK: https://www.w3schools.com/python/python_polymorphism.asp
#######################################################################################################################
pass

#######################################################################################################################
# Modules
# LINK: https://www.w3schools.com/python/python_modules.asp
#######################################################################################################################
pass

#######################################################################################################################
# Built-in Functions
# LINK: https://www.w3schools.com/python/python_ref_functions.asp
#######################################################################################################################
pass

#######################################################################################################################
# Data Time Module
# LINK: https://www.w3schools.com/python/python_datetime.asp
#######################################################################################################################
pass

#######################################################################################################################
# JSON Module
# LINK: https://www.w3schools.com/python/python_json.asp
#######################################################################################################################
pass

#######################################################################################################################
# RegEx Module
# LINK: https://www.w3schools.com/python/python_regex.asp
#######################################################################################################################
pass

#######################################################################################################################
# Math Module
# LINK: https://www.w3schools.com/python/python_math.asp
# LINK: https://www.w3schools.com/python/module_math.asp
#######################################################################################################################
pass

#######################################################################################################################
# Random Module
# LINK: https://www.w3schools.com/python/module_random.asp
#######################################################################################################################
pass

#######################################################################################################################
# CMath Module
# LINK: https://www.w3schools.com/python/module_cmath.asp
#######################################################################################################################
pass

#######################################################################################################################
# Statistics Module
# LINK: https://www.w3schools.com/python/module_statistics.asp
#######################################################################################################################
pass

#######################################################################################################################
# Complete Python Reference
# LINK: https://www.w3schools.com/python/python_reference.asp
#######################################################################################################################
pass

#######################################################################################################################
# File Handling
# LINK: https://www.w3schools.com/python/python_file_handling.asp
# LINK: https://www.w3schools.com/python/python_file_open.asp
# LINK: https://www.w3schools.com/python/python_file_write.asp
# LINK: https://www.w3schools.com/python/python_file_remove.asp
# LINK: https://www.w3schools.com/python/python_ref_file.asp
#######################################################################################################################
pass

#######################################################################################################################
# Python Examples for All scenarios
# LINK: https://www.w3schools.com/python/python_examples.asp
#######################################################################################################################
pass
